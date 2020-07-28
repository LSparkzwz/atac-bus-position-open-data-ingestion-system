import os

def execute_queries(athena):
    get_bus_status(athena)

def get_buse_status(athena):
    query = 'SELECT max(waiting_time) as waiting_time \
    FROM "stops_feed"."stops_feed"'
    output = 'bus_status/'
    execute_query(athena,query,output)



def execute_query(athena,query,output):
    queryStart = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': os.environ['ATHENA_DB']
        },
        ResultConfiguration={
            'OutputLocation': 's3://' + os.environ['BUCKET_NAME'] + '/results/' + output,
        }
    )
    
    
WITH 
i AS (
SELECT b.trip_id, b.route_id, b.lat, b.lon, b.stop_sequence as bus_stop_sequence, st.stop_id, st.stop_sequence
FROM "stops_feed"."bus_feed" as b LEFT OUTER JOIN "stops_feed"."stop_times" as st
ON b.trip_id = st.trip_id
),

n AS (
SELECT i.trip_id, i.route_id, i.lat, i.lon, i.bus_stop_sequence, i.stop_sequence, l.stop_name, l.lat as stop_lat, l.lon as stop_lon
FROM i LEFT OUTER JOIN "stops_feed"."stops" as l
ON i.stop_id = l.stop_id
),

f AS (
SELECT n.lat, n.lon, n.bus_stop_sequence, array_agg(ROW(n.stop_sequence, n.stop_name, n.stop_lat, n.stop_lon)) as route, r.route_name
FROM n LEFT OUTER JOIN "stops_feed"."routes" as r
ON n.route_id = r.route_id
GROUP BY n.trip_id, n.lat, n.lon, n.bus_stop_sequence, r.route_name
)

SELECT array_agg(ROW(f.lat, f.lon, f.bus_stop_sequence)) as buses, arbitrary(route), f.route_name
FROM f
GROUP BY f.route_name
