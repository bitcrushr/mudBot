import json
import requests
import time

#issue the command 'chat_pass' ingame to acquire a temporary 'token'
#run the program once and replace this variable with the long-term token it prints to the console
token = ""

#messages go here, in array form
messages = [""]

#modes: cycle , multi
#cycle - bot will sequentially send messages on a loop, one at a time
#multi - bot will send every message every time it loops
mode = "cycle"

#delay between individual messages in multi mode
#this does nothing if you're using cycle mode
#values below .5 will make the messages display out of order
multi_delay = .5

#must be one of your account's users
username = ""

#selected user must be in this channel
channel = ""

#how long to wait between messages, in seconds
timeout = 1000

def send_request(method, params):
    return requests.post('https://www.hackmud.com/mobile/{}.json'.format(method),
            headers = {'Content-Type': 'application/json'},
            json = params)


if len(token) < 6:
    res = send_request('get_token', { 'pass' : token } ).json()
    token = res['chat_token']
    print("Replace the token variable with this: {}".format(token))

index = 0
running = True

while running:
    if mode == "cycle":
        send_request('create_chat',  { 'chat_token' : token, 'username' : username, 'channel' : channel, 'msg' : messages[index]} ).json()
        index += 1
        if index > len(messages)-1:
            index = 0
    elif mode == "multi":
        for msg in messages:
            send_request('create_chat',  { 'chat_token' : token, 'username' : username, 'channel' : channel, 'msg' : msg} ).json()
            time.sleep(multi_delay)
    time.sleep(timeout)
