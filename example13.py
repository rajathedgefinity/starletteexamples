from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route, Mount
import json

async def homepage(request):
    return PlainTextResponse("HomePage")

async def about(request):
    return PlainTextResponse("About")


#Path Parameters - 1
async def user(request):
    if request.path_params:
        user_id = request.path_params['user_id']
        return PlainTextResponse(str(user_id))
    else:
        return PlainTextResponse("No Parameters!")

#Path Parameters - 2
async def submountex(request):
    if request.path_params:
        username = request.path_params['username']
        return PlainTextResponse(username)
    else:
        return PlainTextResponse("SubMountex")

# Request Methods Received JSON {Body}
# Follow Thread https://github.com/encode/starlette/issues/493
async def firerecv(request):
    if request.method == 'GET':
        return PlainTextResponse("Received GET Method")
    if request.method == 'POST':
        body_bytes = await request.body()
        if body_bytes:
            json = await request.json()
            return JSONResponse(json)
        # print(json.dumps(data))
        return PlainTextResponse("Received POST Method")

routes = [
    Route("/", endpoint=homepage),
    Route("/about", endpoint=about),
    Route("/fire", endpoint=firerecv, methods = ['GET','POST']),
    Route("/users", endpoint=user), # Main Route
    Route("/users/{user_id:int}", endpoint=user),  # Sub Route to Main Route
    Mount("/submex", routes=[
        Route('/{username:str}', endpoint=submountex),
        Route('/', endpoint=submountex)
    ]) # Mounting Multiple SubRoutes after Main Route.
]


app = Starlette(routes=routes)
