import bus_feed as bf
import queries
import os
import boto3

def lambda_handler(event, context):
    bus_feed = bf.update_feed()
    s3 = boto3.resource('s3')
    bf.insert_buses(bus_feed,s3)
    athena = boto3.client('athena')
    queries.execute_queries(athena)




    return {
        'statusCode': 200
    }
