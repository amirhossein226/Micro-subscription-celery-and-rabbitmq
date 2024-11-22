import pika
import json
import requests
from rapidfuzz import fuzz


connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',
    credentials=pika.PlainCredentials(
        'guest',
        'guest'
    )
))

channel = connection.channel()
channel.queue_declare('match_queue', durable=True)
channel.queue_declare('mail_queue', durable=True)


def callback(ch, method, properties, body):
    data = json.loads(body)
    response = requests.get('http://127.0.0.1:8001/api/v1/addresses/')

    addresses = [address['address'] for address in response.json()]

    top_score = 0
    min_score = 70
    matched_address = data['address']
    for address in addresses:
        score = round(fuzz.ratio(address, data['address']))
        if score > top_score and score >= min_score:
            top_score = score
            matched_address = address
        if score == 100:
            break
    print(f'Matched address is ----> {matched_address}')

    if matched_address != data["address"]:
        data.update({'address': matched_address})
    response = requests.post(
        "http://127.0.0.1:8001/api/v1/addresses/", data=data)

    ch.basic_publish(
        exchange='',
        routing_key='mail_queue',
        body=json.dumps(data),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


def run():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='match_queue',
        on_message_callback=callback
    )

    channel.start_consuming()
