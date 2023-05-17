import socket
import threading
from typing import Tuple

# Task 2

HOST = '0.0.0.0'
PORT = 50000


def handle_connection(connection: socket.socket, address: Tuple[str, int]):
    formatted_address = f"{address[0]}:{address[1]}"
    with connection:
        print('Connected by', formatted_address)
        while True:
            try:
                data = connection.recv(1024)
            except ConnectionError:
                break
            if not data:
                break
            try:
                connection.sendall(data)
            except Exception as e:
                print(e)
    print('Disconnected by', formatted_address)


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"He is alive on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print("Connection is here", addr)
            my_thread = threading.Thread(target=handle_connection, args=(conn, addr), daemon=True)
            my_thread.start()
