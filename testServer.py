import threading

from rdt import RDTSocket

server_addr = ('127.0.0.1', 2130)


class Echo(threading.Thread):
    def __init__(self, conn: RDTSocket, address):
        threading.Thread.__init__(self)
        self.conn = conn
        self.address = address

    def run(self):
        while True:
            data = self.conn.recv(2048)
            print(data)
            break


def main():
    server_socket = RDTSocket()
    server_socket.bind(server_addr)
    while True:
        conn, addr = server_socket.accept()
        print(addr)
        Echo(conn, addr).start()


if __name__ == '__main__':
    main()
