import requests
import json

class HipchatApi():


    def send_message(url, msg, notify = "false", color = "green", message_format = "text"):
        params = {
            "message": msg[:9999],
            'notify': notify,
            'color': color,
            'message_format': message_format
        } 
        
        r=requests.post(url, data=json.dumps(params), headers={'Content-Type': 'application/json'})
        if r.status_code >= 400:
            raise Exception('Не удалось отправить сообщение о комментарии {0} {1}'.format(msg, r.json()['error']))



