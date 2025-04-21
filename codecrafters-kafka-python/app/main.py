import socket  # noqa: F401
import struct

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    # server.accept() # wait for client
    server_socket, _ = server.accept()
    # server_socket.sendall(b"7")
    while server_socket.recv(1024):
        data = struct.pack(">II", 0, 7) # b'\x00\x00\x00\x00\x00\x00\x00\x07'
        # ">" = big-endian (network byte order); the most significant byte goes first 
        # "I" = unsigned 32-bit integer; 4 bytes; 
        # "II" = packing 2 integers back-to-back
        print(data.hex()) # 0000000000000007
        server_socket.sendall(data)


if __name__ == "__main__":
    main()
