import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',
    credentials=pika.PlainCredentials(
        'guest',
        'guest'
    )
))

channel = connection.channel()
channel.queue_declare('match_queue', durable=True)


def match_address_task(user_info):
    channel.basic_publish(
        exchange='',
        routing_key='match_queue',
        body=json.dumps(user_info),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
