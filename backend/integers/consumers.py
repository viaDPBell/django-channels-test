import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({"message": randint(1, 100)}))
            sleep(1)

    # def receive(self, text_data=None, bytes_data=None):
    #     return super().receive(text_data, bytes_data)
