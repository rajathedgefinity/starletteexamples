from starlette.responses import FileResponse

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = FileResponse('static/favicon.ico')
    await response(scope, receive, send)
    
