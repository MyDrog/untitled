import requests
from time import sleep
url = "https://api.telegram.org/bot432501879:AAGx9FEXS376mQYnXOzViWAe4tqhtgpb-0Q/"
ids=set()
def inf(requst):
    params = {'timeout': 100, 'offset': None}
    r = requests.get(url+'getUpdates',data=params)
    return r.json()


def lastupdate(data):
    result= data['result']
    tu=len(result)-1
    return result[tu]

def res(data):
    result = data['result']

    return result


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id
def sendmessage(chat,text):
    params = {'chat_id':chat,'text':text}
    r = requests.post(url+'sendMessage',data=params)
    return r


def main():
    for x in res(inf(url)):
        ids.add(x['message']['chat']['id'])
    while True:
        for id in ids:
            sendmessage(id, 'НАВАЛЬНЫЙ 20!8')
            sleep(0.001)

main()


