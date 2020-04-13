import time
import socketio
import json

sio = socketio.Client(engineio_logger=True)

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

@sio.on('book_BTC_USD')
def depth(data):
    print(data)

# @sio.on('type')
# def deal(data):
#     print('deal received with ', data)

# @sio.on('push.symbol')
# def sub(data):
#     print('sub received with ', data)




sio.connect('wss://btc-alpha.com', transports=['websocket'])
# sio.emit('sub.symbol', {'symbol': 'BTC_USD'})
# sio.emit('book_BTC_USD')


sio.wait()  # 不发心跳，可以保持连接接收消息

