from starlette.responses import StreamingResponse
import asyncio

async def slow_numbers(minimum, maximum):
    yield('<html><body><ul>')
    for number in range(minimum, maximum +1):
        yield '<li>%d</li>' % number
        await asyncio.sleep(0.5)
    yield('</ul></body></html>')

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    generator = slow_numbers(1,10)
    response = StreamingResponse(generator, media_type='text/html')
    await response(scope, receive, send)
