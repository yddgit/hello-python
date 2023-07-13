import asyncio
import threading


# asyncio.coroutine会把一个generator标记为coroutine类型
# @asyncio.coroutine
# def hello():
#     print('Hello world!')
#     r = yield from asyncio.sleep(1)
#     print('Hello again')
#
#
# loop = asyncio.get_event_loop()  # 获取EventLoop
# loop.run_until_complete(hello())  # 执行coroutine
# loop.close()


# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.current_thread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.current_thread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s ...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.google.com', 'cn.bing.com', 'www.baidu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
