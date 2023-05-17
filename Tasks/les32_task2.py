import socket

HOST = '0.0.0.0'
PORT = 50000


def encryption_decryption(language, shift_step, txt):
    if language == 'ang':
        alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
        moch = 26
    elif language == 'ru':
        alphabet = [chr(i) for i in range(1040, 1104)]
        moch = 32
    for i in range(len(txt)):
        if txt[i].isalpha():
            if txt[i].isupper():
                return alphabet[(alphabet.index(txt[i]) + shift_step) % moch]
            else:
                return alphabet[(alphabet.index(txt[i]) + shift_step) % moch + moch]
        else:
            return txt[i]


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
                text, step  = data
                connection.sendall(encryption_decryption('eng', step, text))
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
            handle_connection(conn, addr)
