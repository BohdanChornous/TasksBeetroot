import socket

HOST = '0.0.0.0'
PORT = 50000

def handle_connection(mess: socket.socket, address: Tuple[str, int], s: socket.socket):
    formatted_address = f"{address[0]}:{address[1]}"
    print('Connected by', formatted_address)
    try:
        data = mess.recv(1024)
    except ConnectionError as e:
        return e
    if not data:
        return "No message!!"
    try:
        s.sendto("General Kenobi".encode("uft-8", address))
    except Exception as e:
        print(e)
    print('Disconnected by', formatted_address)


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            message, addr = s.recvfrom(1024)
            print("Connection is here", addr)
            handle_connection(message, addr, s)