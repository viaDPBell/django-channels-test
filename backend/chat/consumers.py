import json

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer

from channels.generic.websocket import AsyncWebsocketConsumer


# 비동기식 ChatConsumer
# I/O를 수행하는 비동기 함수를 호출하는데 사용
# async_to_sync 메서드가 필요없음
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message", "message": message})

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))


# 동기식 ChatConsumer
"""
# 사용자가 메세지를 보내면 JavaScript에서 WebSocket을 통해 ChatConsumer로 전송
# ChatConsumer는 해당 메시지를 수신하여 방 이름에 해당하는 그룹에 전달
# 같은 그룹(같은 방에 있는) 모든 ChatConsumer는 그룹에서 메시지를 수신하고 WebSocket을 통해 다시 JavaScript로 전달하여 채팅 로그에 추가
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # self.accept()
        # Cunsumer에 대한 WebSocket 연결을 연 "room_name" URL 경로(chat/routing.py)에서 매개변수를 가져옴
        # 모든 Cunsumer는 scope를 갖고 있음. scope는 URL 경로의 위치 또는 키워드 인수와 현재 인증된 사용자(있을 경우)를 포함하여 연결에 대한 모든 정보를 포함
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        # Consumer 지정 룸 이름에서 직접 채널 그룹 이름을 구성
        # 그룸 이름에는 영숫자, 하이픈, 밑줄 또는 마침표만 사용할 수 있음
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        # 그룹에 가입
        # ChatConsumer는 동기식 WebsocketConsumer지만 비동기식 채널 레이어 메서드를 호출하기 때문에 async_to_sync 래퍼가 필요함(모든 채널 계층은 비동기식으로 동작)
        # 그룹 이름은 ASCII 영숫자, 하이픈 및 마침표로만 제한되고 기본 백엔드에서 최대 길이는 100으로 제한되어있음
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        # WebSocket 연결을 수락
        # connect 메서드 내에서 accept()를 호출하지 않으면 연결이 거부되고 닫히게 됨
        # 예로 요청 사용자가 요청된 작업을 수행할 수 있는 권한이 없으면 연결 거부 가능
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        # 그룹을 떠남
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # self.send(text_data=json.dumps({"message": message}))

        # Send message to room group
        # 그룹에 이벤트를 보냄
        # 이벤트에는 이벤트를 수신하는 Consumer에서 호출해야하는 메서드 이름에 해당하는 "type"이 있습니다.
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "chat.message", "message": message})

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
"""
