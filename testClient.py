from rdt import RDTSocket

server_addr = ('127.0.0.1', 2130)


def main():
    socket = RDTSocket()
    socket.connect(server_addr)
    socket.send(b'hello')


if __name__ == '__main__':
    main()
