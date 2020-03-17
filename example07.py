from starlette.responses import Response

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = Response("Hello World!", status_code=200, media_type='text/plain')
    await response(scope, receive, send)
