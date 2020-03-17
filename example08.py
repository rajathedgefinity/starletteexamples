# from starlette.responses import HTMLResponse
#
# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#     response = HTMLResponse('<html><body><h3>Hello World!,</h3></body></html>')
#     await response(scope, receive, send)


# from starlette.responses import PlainTextResponse
#
# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#     response = PlainTextResponse('Hello World!')
#     await response(scope, receive, send)

# from starlette.responses import JSONResponse
#
# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#     response = JSONResponse({'hello':'world'})
#     await response(scope, receive, send)

from starlette.responses import UJSONResponse

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = UJSONResponse({'hello':'world'})
    await response(scope, receive, send)
