from starlette.responses import PlainTextResponse, RedirectResponse

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    if scope['path'] != '/':
        response = RedirectResponse(url='/')
    else:
        response = PlainTextResponse('Hello World!')
    await response(scope, receive, send)
