import socket  # noqa: F401
import struct

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    # Task 2
    # server.accept() # wait for client
    # server_socket, _ = server.accept()
    # # server_socket.sendall(b"7")
    # while server_socket.recv(1024):
    #     data = struct.pack(">II", 0, 7) # b'\x00\x00\x00\x00\x00\x00\x00\x07'
    #     # ">" = big-endian (network byte order); the most significant byte goes first 
    #     # "I" = unsigned 32-bit integer; 4 bytes; 
    #     # "II" = packing 2 integers back-to-back
    #     print(data.hex()) # 0000000000000007
    #     server_socket.sendall(data)

    # Task 3
    # request => $ echo -n "00000023001200046f7fc66100096b61666b612d636c69000a6b61666b612d636c6904302e3100" | xxd -r -p | nc localhost 9092 | hexdump -C
    # response => 00 00 00 00  // message_size:   0 (any value works)
    #             6f 7f c6 61  // correlation_id: 1870644833
    server_socket, _ = server.accept()
    while raw_request := server_socket.recv(1024):
        correlation_id = raw_request[8:12]
        print(f"correlation_id: {correlation_id}")
        correlation_id = int.from_bytes(correlation_id, byteorder="big")
        print(f"correlation_id: {correlation_id}")
        
        # print(f"raw_request: {raw_request};") # decoded_request: {raw_request.decode()}; raw_request_hex: {raw_request.hex()}; correlation_id: {correlation_id}")
        print(f"raw_request: {raw_request}; raw_request_hex: {raw_request.hex()}; correlation_id: {correlation_id}")
        data = struct.pack(">II", 0, correlation_id)
        print(f"data: {data}")
        server_socket.sendall(data)


if __name__ == "__main__":
    main()
