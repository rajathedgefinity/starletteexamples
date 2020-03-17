from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    form = await request.form()
    filename = form["upload_file"].filename
    contents = await form["upload_file"].read()
    response = Response(contents, media_type='text/plain')
    await response(scope, receive, send)
