import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def random_number(number):
    print(f'Receied random number: {number}')

@sio.event
def disconnect():
    print('Disconnected from server')

if __name__ == '__main__':
    server_url = 'http://localhost:5000'
    print(f'Conncting to server at {server_url}')
    sio.connect(server_url)
    sio.wait()
