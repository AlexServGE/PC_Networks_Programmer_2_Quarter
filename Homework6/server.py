import socket
import threading

HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
cache_host_connections = list()


def get_mess():
    global s
    global cache_host_connections
    conn, addr = s.accept()
    cache_host_connections.append(conn)
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            print(data.decode(encoding='ascii'))
            for el in cache_host_connections:
                el.sendall(data)


get_thread_1 = threading.Thread(target=get_mess)
get_thread_2 = threading.Thread(target=get_mess)
get_thread_1.start()
get_thread_2.start()
