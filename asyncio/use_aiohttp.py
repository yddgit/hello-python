import asyncio
from aiohttp import web

# pip install aiohttp


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(content_type='text/html', charset='utf-8', body=b'<h1>Index</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(content_type='text/html', charset='utf-8', body=text.encode('utf-8'))


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await loop.create_server(app_runner.server, '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000/ ...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
