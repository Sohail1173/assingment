import random
import socketio
import eventlet


sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('Client connected')

@sio.event
def disconnect(sid):
    print('Client disconnected')

@sio.event
def random_value(sid):
    value = random.randint(1, 100)
    print('Server generated random value:', value)
    sio.emit('random_value', value)
    
if __name__ == '__main__':
    port = 5000
    print('Starting server on port', port)
    eventlet.wsgi.server(eventlet.listen(('', port)), app)
