from django.shortcuts import render
import requests
import logging


def say_hello(request):
    try:
        logging.info('Calling httpbin')
        requests.get('https://httpbin.org/delay/2')
        logging.info('Received the response')
    except request.ConnectionError:
        logging.critical('httpbin is down')
    return render(request, 'hello.html', {'name': 'Mosh'})
