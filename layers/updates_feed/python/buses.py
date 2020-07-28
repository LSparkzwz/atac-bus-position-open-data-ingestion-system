import os
import string
import csv
import boto3

def insert_buses(feed, s3):
    with open('/tmp/bus_feed.csv', 'w+', newline='\n') as output:
        writer = csv.writer(output)
        for entity in feed:
            vehicle = entity.vehicle
            trip_id = str(vehicle.trip.trip_id)
            route_id = str(vehicle.trip.route_id)
            lat = vehicle.position.latitude
            lon = vehicle.position.longitude
            stop_sequence = vehicle.current_stop_sequence
            if trip_id != '' or route_id != '' or stop_sequence != 0 :
                writer.writerow(
                    [trip_id, route_id, lat, lon, stop_sequence])
    bucket = os.environ['BUCKET_NAME']
    s3.Object(bucket, "bus/bus_feed.csv").put(Body=open('/tmp/bus_feed.csv', 'rb'))
