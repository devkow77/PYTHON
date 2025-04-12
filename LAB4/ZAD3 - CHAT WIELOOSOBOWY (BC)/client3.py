import socket
import threading

HOST = 'localhost'
PORT = 50007


def receive_messages(s):
    """Nasłuchuje wiadomości od serwera."""
    while True:
        try:
            msg = s.recv(1024).decode('utf-8')
            if not msg:
                break
            print(msg)
        except:
            print("❌ Rozłączono z serwerem.")
            break


def start_client():
    """Uruchamia klienta."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        threading.Thread(target=receive_messages, args=(s,), daemon=True).start()

        while True:
            msg = input()
            if msg.lower() == "/exit":
                break
            s.sendall(msg.encode('utf-8'))


if __name__ == "__main__":
    start_client()
