import os
import httpx

def redirect(payload):
    CAST_SERVICE_HOST_URL = 'http://localhost:8080/add'

    url = CAST_SERVICE_HOST_URL
    req = httpx.post(url, data = payload)
