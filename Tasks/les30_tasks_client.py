import socket
import threading
import time

FORMAT = "utf-8"
HOST = '127.0.0.1'
PORT = 50000


def receive():
    while True:
        data = s.recv(1024)
        if data is None or data == b"" or not data:
            break
        print(f"\r{data.decode()}")
        print('Enter massage: ', end="")


def send_massage():
    while True:
        letter = input("Enter massage: ")
        if not letter:
            continue
        s.sendall(letter.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send_tr = threading.Thread(target=send_massage, daemon=True)
    rec_tr = threading.Thread(target=receive, daemon=True)
    send_tr.start()
    rec_tr.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
