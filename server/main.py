
import os
import ssl
import asyncio
import uvloop
from sanic import Sanic
from sanic import response
from server import messagehub

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


app = Sanic()


@app.route('/', methods=['GET'])
async def handle_request(request):
    return response.text(messagehub.handleGet())

@app.route('/add/<name>', methods=['GET'])
async def handle_request(request, name):
    return response.text(messagehub.handleAdd(name))

@app.route('/rage/add/<name>', methods=['GET'])
async def handle_request(request, name):
    return response.text(messagehub.handleAddRage(name))

@app.route('/rage/get/', methods=['GET'])
async def handle_request(request):
    return response.text(messagehub.handleGetRage())

@app.route('/clear/123', methods=['GET'])
async def handle_request(request):
    return response.text(messagehub.handleClear())


if __name__ == '__main__':
    
    messagehub.setup();

    print(ssl.OPENSSL_VERSION)
    
    hostAddr = '0.0.0.0'

    certDir = ''

    app.run(host=hostAddr, port=8070, workers=1)
