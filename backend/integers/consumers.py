import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    connected_clients = set()

    def connect(self):
        self.accept()
        self.connected_clients.add(self)

        for i in range(1000):
            self.send(json.dumps({"message": randint(1, 100)}))
            sleep(1)

    # def disconnect(self, code):
    #     if self.channel_name in self.connected_clients:
    #         self.connected_clients.remove(self)
    #     self.close(code=code)

    # def receive(self, text_data=None, bytes_data=None):
    #     return super().receive(text_data, bytes_data)


# import json
# from random import randint

# # from time import sleep
# import asyncio

# from channels.generic.websocket import WebsocketConsumer


# class WSConsumer(WebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#         for i in range(1000):
#             await self.send(json.dumps({"message": randint(1, 100)}))
#             # sleep(1)
#             await asyncio.sleep(1)

#     # def receive(self, text_data=None, bytes_data=None):
#     #     return super().receive(text_data, bytes_data)
