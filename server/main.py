
import os
import ssl
import asyncio
import uvloop
from sanic import Sanic
from sanic import response
from server.messagehub import *

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


app = Sanic()


@app.route('/', methods=['GET'])
async def handle_request(request):
    return response.text(handleGet())

@app.route('/add/<name>', methods=['GET'])
async def handle_request(request, name):
    return response.text(handleAdd(name))

@app.route('/clear/123', methods=['GET'])
async def handle_request(request):
    return response.text(handleClear())


if __name__ == '__main__':
    
    print(ssl.OPENSSL_VERSION)
    
    hostAddr = '0.0.0.0'

    certDir = ''

    #test if we are running on the server
    try:
        with open('is_server', 'r') as isServerFile:
            certDir = '/etc/letsencrypt/live/azenix.io/'
    except FileNotFoundError:
        print("not running on server")

    certPath = os.path.join(certDir, 'fullchain.pem')
    keyPath = os.path.join(certDir, 'privkey.pem')
    
    print("cert path: " + str(certPath))
    print("key path: " + str(keyPath))

    ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
    # ctx.verify_mode = ssl.CERT_REQUIRED
    # ctx.load_verify_locations(os.path.join(CERT_DIR, 'CA.crt'))
    ctx.load_cert_chain(
        certfile=certPath,
        keyfile=keyPath
    )   
    app.run(host=hostAddr, port=443, ssl=ctx, workers=4)
