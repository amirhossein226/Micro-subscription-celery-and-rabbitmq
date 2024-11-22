import pika
import json
from django.core.mail import send_mail


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=pika.PlainCredentials(
            'guest',
            'guest'
        )
    )
)

channel = connection.channel()
channel.queue_declare('mail_queue', durable=True)


def callback(ch, method, properties, body):
    mail_message = json.loads(body)
    send_mail(
        'Your subscription.',
        f'Dear {mail_message['name']}.we received your subscription and will send our newest magazines\
to *{mail_message['address']}*',
        'rabbit@gmail.com',
        [mail_message['email']],
        fail_silently=False
    )


def run():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='mail_queue',
        on_message_callback=callback
    )

    channel.start_consuming()
