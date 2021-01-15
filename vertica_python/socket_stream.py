import ssl


class SocketStream(object):
    def __init__(self, raw_socket, buffer_size):
        self.socket = raw_socket
        self.socket_io = raw_socket.makefile('rwb', buffer_size)

    def close(self):
        self.socket_io.close()
        self.socket.close()

    def is_ssl(self):
        return isinstance(self.socket, ssl.SSLSocket)

    def __getattr__(self, attr):
        return getattr(self.socket_io, attr)

    def __str__(self):
        return '<SocketStream:{0} socket={1}>'.format(id(self), self.socket)
