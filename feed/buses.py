import string
from google.transit import gtfs_realtime_pb2
import csv

feed1 = gtfs_realtime_pb2.FeedMessage()
with open("bus_feed.csv","rb") as source:
    feed = feed1.ParseFromString( source )
    print feed
    with open('buses.csv', 'w+') as output:
        writer = csv.writer(output)
        for entity in feed.entity:
            vehicle = entity.vehicle
            trip_id = str(vehicle.trip.trip_id)
            route_id = str(vehicle.trip.route_id)
            lat = vehicle.position.latitude
            lon = vehicle.position.longitude
            stop_sequence = vehicle.current_stop_sequence
            if trip_id != '' or route_id != '' or stop_sequence != 0 :
                writer.writerow(
                    [trip_id, route_id, lat, lon, stop_sequence])
            
    
