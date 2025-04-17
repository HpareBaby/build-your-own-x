import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client
    # server_socket.accept
    # server_socket.accept()[0].sendall("HTTP/1.1 200 OK\r\n\r\n".encode()) # task 2
    
    # task 3
    # client_conn, address = server_socket.accept()
    # print("client_conn.recv")
    # print(client_conn.recv(4096)) # WRONG: it reads all http request already; calling it the second time will make the server wait forever
    # raw_request = client_conn.recv(4096).decode() #.decode('utf-8', errors='replace')
    # print("after raw_request")
    # print(raw_request)

    # the following code block works successfully
    # #method, request_path = raw_request.splitlines()[0].split()[:2]
    # method, request_path = raw_request.split(" ")[:2]
    # print(f"method: {method}")
    # print(f"request_path: {request_path}")
    # response = "HTTP/1.1 404 Not Found\r\n\r\n"
    # if (method == "GET") & (request_path == "/"):
    #     response = "HTTP/1.1 200 OK\r\n\r\n"
    
    # the following code block works successfully
    # request = raw_request.split(" ")
    # response = "HTTP/1.1 404 Not Found\r\n\r\n"
    # if (request[1] == "/"):
    #     response = "HTTP/1.1 200 OK\r\n\r\n"
    # print(f"response: {response}")
    # client_conn.sendall(response.encode())


    # task 4
    client_conn, address = server_socket.accept()
    raw_request = client_conn.recv(4096).decode()
    print(f"raw_request: {raw_request}")
    request = raw_request.split(" ")
    request_path = request[1].split("/")
    response = "HTTP/1.1 404 Not Found\r\n\r\n"
    if (request[0] == "GET") & (request[1] == "/"):
        response = "HTTP/1.1 200 OK\r\n\r\n"
    elif (request[0] == "GET") & (request_path[1] == "echo"):
        request_msg = request_path[2]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    print(f"request: {request}")
    print(f"request_path: {request_path}")
    print(f"response: {response}")
    client_conn.sendall(response.encode())

if __name__ == "__main__":
    main()
