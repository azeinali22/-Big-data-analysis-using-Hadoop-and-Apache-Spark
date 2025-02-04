import socket
import time


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 4000))
    server_socket.listen(1)
    print("Server listening on port 5000...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} established.")

    # Sending names
    names = ["Alice", "Bob", "Charlie", "David"]
    for name in names:
        conn.sendall(name.encode('utf-8'))
        print(f"Sent: {name}")
        time.sleep(1)  # Send a name every second

    conn.close()
    server_socket.close()


if __name__ == '__main__':
    start_server()
