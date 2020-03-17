from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    body = b''
    async for chunk in request.stream():
        body += chunk
    response = Response(body, media_type='text/plain')
    await response(scope, receive, send)
