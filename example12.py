from starlette.websockets import WebSocket

async def app(self, scope, receive, send):
    websocket = WebSocket(scope=scope, receive=receive, send=send)
    await websocket.accept()
    await websocket.send_text('Hello World!')
    await websocket.close()
    
