from google.transit import gtfs_realtime_pb2
import urllib
import sys
import csv
import string
import json
import time

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('https://romamobilita.it/sites/default/files/rome_rtgtfs_vehicle_positions_feed.pb')
feed.ParseFromString(response.read())
with open('vehicle.csv', 'w') as f:
    writer = csv.writer(f)
    for entity in feed.entity:
            vehicle = entity.vehicle
            trip_id = str(vehicle.trip.trip_id)
            route_id = str(vehicle.trip.route_id)
            lat = vehicle.position.latitude
            lon = vehicle.position.longitude
            stop_sequence = vehicle.current_stop_sequence
            if trip_id != '' or route_id != '' or stop_sequence != 0 :
                writer.writerow([trip_id, route_id, lat, lon, stop_sequence])


feed2 = gtfs_realtime_pb2.FeedMessage()
response2 = urllib.urlopen('https://romamobilita.it/sites/default/files/rome_rtgtfs_service_alerts_feed.pb')
feed2.ParseFromString(response2.read())
with open('alerts.json', 'w') as c:
    writer = csv.writer(c)
    data = {}
    for entity in feed2.entity:
            alert = entity.alert
            start = alert.active_period[0].start
            end = alert.active_period[0].end
            route_id = str(alert.informed_entity[0].route_id)
            print alert.cause
            print alert.effect
            cause = str(alert.cause)
            effect = str(alert.effect)
            description = str(alert.header_text.translation[0].text.encode("utf-8"))
            details = str(alert.description_text.translation[0].text.encode("utf-8"))
            out = [start, end, cause, effect, description, details]
            if route_id in data:
                data[route_id].append(out)
            else:
                data[route_id] = [out]
    json.dump(data, c)
