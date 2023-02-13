import socket
import threading

host_socket = socket.socket()
server_socket = ('127.0.0.1', 50007)

host_socket.connect(server_socket)

nickname = 'AlexServGE_2'
host_socket.send(nickname.encode(encoding='ascii'))


def send_mess():
    while True:
        mes = input()
        text_to_send = f'{nickname}:{mes}'.encode(encoding='ascii')
        host_socket.send(text_to_send)


def get_mess():
    while True:
        text = host_socket.recv(1024)
        print(text.decode(encoding='ascii'))


send_thread = threading.Thread(target=send_mess)
get_thread = threading.Thread(target=get_mess)
send_thread.start()
get_thread.start()
