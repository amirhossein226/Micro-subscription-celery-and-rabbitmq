from celery import shared_task
from django.core.mail import send_mail
from rapidfuzz import fuzz
import requests


@shared_task
def match_address_task(data):
    response = requests.get('http://127.0.0.1:8001/api/v1/addresses/')
    addresses = [a['address'] for a in response.json()]

    top_score = 0
    min_score = 70
    matched_address = data['address']
    for address in addresses:
        score = round(fuzz.ratio(data['address'], address))
        if score > top_score and score >= min_score:
            top_score = score
            matched_address = address
        if score == 100:
            break
    print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>\
          matched address is {matched_address}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if matched_address != data['address']:
        data.update({'address': matched_address})
    response = requests.post(
        'http://127.0.0.1:8001/api/v1/addresses/', data=data)

    send_email_task.delay(data)


@shared_task
def send_email_task(email_details):
    send_mail(
        'Your subscription',
        f"Dear {email_details['name']}. \
            We received your subscription and will send our newest magazines to {email_details['address']}",
        'celery@gmail.com',
        [{email_details['email']}],
        fail_silently=False
    )
