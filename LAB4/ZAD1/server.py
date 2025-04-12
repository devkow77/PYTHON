import socket
from datetime import datetime

HOST = 'localhost'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()

    while conn:
        print(f"Server is listening at: {addr}")
        # odebranie wiadomosci od klienta
        res = conn.recv(1024).decode("utf-8").lower()
        msg = ""
        if res == "hello":
            msg = "Hello from server"
        elif res == "time":
            msg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            msg = "Unknow command"

        conn.sendall(msg.encode("utf-8"))



