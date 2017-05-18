import json
import requests
import time

token = ""
messages = [
""
]
username = ""
channel = ""

timeout = 1000

running = True

def send_request(method, params):
    return requests.post('https://www.hackmud.com/mobile/{}.json'.format(method),
            headers = {'Content-Type': 'application/json'},
            json = params)


if len(token) < 6:
    res = send_request('get_token', { 'pass' : token } ).json()
    token = res['chat_token']
    print("Replace the token variable with this: {}".format(token))

while running:
    for msg in messages:
        send_request('create_chat',  { 'chat_token' : token, 'username' : username, 'channel' : channel, 'msg' : msg} ).json()
    time.sleep(timeout)
