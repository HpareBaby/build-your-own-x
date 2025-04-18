import socket  # noqa: F401
import sys

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
    # client_conn, address = server_socket.accept()
    # raw_request = client_conn.recv(4096).decode()
    # print(f"raw_request: {raw_request}")
    # request = raw_request.split(" ")
    # request_path = request[1].split("/")
    # response = "HTTP/1.1 404 Not Found\r\n\r\n"
    # if (request[0] == "GET") & (request[1] == "/"):
    #     response = "HTTP/1.1 200 OK\r\n\r\n"
    # elif (request[0] == "GET") & (request_path[1] == "echo"):
    #     request_msg = request_path[2]
    #     response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    # print(f"request: {request}")
    # print(f"request_path: {request_path}")
    # print(f"response: {response}")
    # client_conn.sendall(response.encode())


    # task 5
    # client_conn, address = server_socket.accept()
    # raw_request = client_conn.recv(4096).decode()
    # print(f"raw_request: {raw_request}")
    # request = raw_request.split(" ")
    # request_path = request[1].split("/")
    # response = "HTTP/1.1 404 Not Found\r\n\r\n"
    # if (request[0] == "GET") & (request[1] == "/"):
    #     response = "HTTP/1.1 200 OK\r\n\r\n"
    # elif (request[0] == "GET") & (request_path[1] == "echo"):
    #     request_msg = request_path[2]
    #     response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    # elif (request[0] == "GET") & (request[1] == "/user-agent"):
    #     # print([n.split(" ") for n in raw_request.splitlines()[1:-1]])
    #     # print({ n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] })
    #     headers = { n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] }
    #     user_agent = headers['User-Agent']
    #     response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    # print(f"request: {request}")
    # print(f"request_path: {request_path}")
    # print(f"response: {response}")
    # client_conn.sendall(response.encode())


    # task 6
    # from concurrent.futures import ThreadPoolExecutor
    # def handle_client(client_conn):
    #     with client_conn:
    #         raw_request = client_conn.recv(4096).decode()
    #         print(f"raw_request: {raw_request}")
    #         request = raw_request.split(" ")
    #         request_path = request[1].split("/")
    #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    #         if (request[0] == "GET") & (request[1] == "/"):
    #             response = "HTTP/1.1 200 OK\r\n\r\n"
    #         elif (request[0] == "GET") & (request_path[1] == "echo"):
    #             request_msg = request_path[2]
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    #         elif (request[0] == "GET") & (request[1] == "/user-agent"):
    #             # print([n.split(" ") for n in raw_request.splitlines()[1:-1]])
    #             # print({ n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] })
    #             headers = { n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] }
    #             user_agent = headers['User-Agent']
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    #         print(f"request: {request}")
    #         print(f"request_path: {request_path}")
    #         print(f"response: {response}")
    #         client_conn.sendall(response.encode())
    # with ThreadPoolExecutor(max_workers=10) as pool:
    #     while True:
    #         client_conn, _ = server_socket.accept()
    #         pool.submit(handle_client, client_conn)
    

    # task 7 
    # from concurrent.futures import ThreadPoolExecutor
    # def handle_client(client_conn):
    #     with client_conn:
    #         raw_request = client_conn.recv(4096).decode()
    #         print(f"raw_request: {raw_request}")
    #         request = raw_request.split(" ")
    #         request_path = request[1].split("/")
    #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    #         if (request[0] == "GET") & (request[1] == "/"):
    #             response = "HTTP/1.1 200 OK\r\n\r\n"
    #         elif (request[0] == "GET") & (request_path[1] == "echo"):
    #             request_msg = request_path[2]
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    #         elif (request[0] == "GET") & (request[1] == "/user-agent"):
    #             # print([n.split(" ") for n in raw_request.splitlines()[1:-1]])
    #             # print({ n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] })
    #             headers = { n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] }
    #             user_agent = headers['User-Agent']
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    #         elif (request[0] == "GET") & (request_path[1] == "files"):
    #             # file_path = "/tmp/{}".format(request_path[2])
    #             # args = sys.argv[1:]
    #             print("args: {}".format(sys.argv))
    #             dir_path = sys.argv[2] if len(sys.argv) > 2 else ''
    #             file_path = "{}{}".format(dir_path, request_path[2])
    #             print(f"dir_path: {dir_path}")
    #             try:
    #                 with open(file_path, 'r') as f:
    #                     content = f.read()
    #                     length = len(content)
    #                     print(f"content: {content}; length: {length}")
    #                 response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {length}\r\n\r\n{content}"
    #             except Exception as e:
    #                 print(e)
    #         print(f"request: {request}")
    #         print(f"request_path: {request_path}")
    #         print(f"response: {response}")
    #         client_conn.sendall(response.encode())
    # with ThreadPoolExecutor(max_workers=10) as pool:
    #     while True:
    #         client_conn, _ = server_socket.accept()
    #         pool.submit(handle_client, client_conn)


    # task 8 
    # from concurrent.futures import ThreadPoolExecutor
    # def handle_client(client_conn):
    #     with client_conn:
    #         raw_request = client_conn.recv(4096).decode()
    #         print(f"raw_request: {raw_request}")
    #         request = raw_request.split(" ")
    #         request_path = request[1].split("/")
    #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    #         if (request[0] == "GET") & (request[1] == "/"):
    #             response = "HTTP/1.1 200 OK\r\n\r\n"
    #         elif (request[0] == "GET") & (request_path[1] == "echo"):
    #             request_msg = request_path[2]
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    #         elif (request[0] == "GET") & (request[1] == "/user-agent"):
    #             # print([n.split(" ") for n in raw_request.splitlines()[1:-1]])
    #             # print({ n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] })
    #             headers = { n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] }
    #             user_agent = headers['User-Agent']
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    #         elif (request[0] == "GET") & (request_path[1] == "files"):
    #             # file_path = "/tmp/{}".format(request_path[2])
    #             # args = sys.argv[1:]
    #             print("args: {}".format(sys.argv))
    #             dir_path = sys.argv[2] if len(sys.argv) > 2 else ''
    #             file_path = "{}{}".format(dir_path, request_path[2])
    #             print(f"dir_path: {dir_path}")
    #             try:
    #                 with open(file_path, 'r') as f:
    #                     content = f.read()
    #                     length = len(content)
    #                     print(f"content: {content}; length: {length}")
    #                 response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {length}\r\n\r\n{content}"
    #             except Exception as e:
    #                 print(e)
    #         elif (request[0] == "POST") & (request_path[1] == "files"):
    #             print("args: {}".format(sys.argv))
    #             dir_path = sys.argv[2] if len(sys.argv) > 2 else ''
    #             file_path = "{}{}".format(dir_path, request_path[2])
    #             content = raw_request.splitlines()[-1]
    #             print(f"content: {content}")
    #             try:
    #                 with open(file_path, 'w') as f:
    #                     f.write(content)
    #                 response = "HTTP/1.1 201 Created\r\n\r\n"
    #             except Exception as e:
    #                 print(e)
    #         print(f"request: {request}")
    #         print(f"request_path: {request_path}")
    #         print(f"response: {response}")
    #         client_conn.sendall(response.encode())
    # with ThreadPoolExecutor(max_workers=10) as pool:
    #     while True:
    #         client_conn, _ = server_socket.accept()
    #         pool.submit(handle_client, client_conn)
    

    # task 9
    # from concurrent.futures import ThreadPoolExecutor
    # def handle_client(client_conn):
    #     with client_conn:
    #         raw_request = client_conn.recv(4096).decode()
    #         print(f"raw_request: {raw_request}")
    #         request = raw_request.split(" ")
    #         request_path = request[1].split("/")
    #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    #         # print(f"request: {request}")
    #         # print(f"request_path: {request_path}")
    #         # print("raw_request: {}".format(raw_request.splitlines()))
    #         headers = { n.split(": ")[0]: n.split(" ")[1] for n in raw_request.splitlines()[1:-1] if len(n) > 1}
    #         # print(f"headers: {headers}")
    #         content_encoding = headers.get('Accept-Encoding')
    #         ce_response = "\r\n"
    #         if content_encoding == "gzip":
    #             ce_response = "\r\nContent-Encoding: gzip\r\n"
            
    #         if (request[0] == "GET") & (request[1] == "/"):
    #             response = "HTTP/1.1 200 OK\r\n\r\n"
    #         elif (request[0] == "GET") & (request_path[1] == "echo"):
    #             request_msg = request_path[2]
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain{ce_response}Content-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    #         elif (request[0] == "GET") & (request[1] == "/user-agent"):
    #             user_agent = headers['User-Agent']
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain{ce_response}Content-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    #         elif (request_path[1] == "files"):
    #             print("args: {}".format(sys.argv))
    #             dir_path = sys.argv[2] if len(sys.argv) > 2 else ''
    #             file_path = "{}{}".format(dir_path, request_path[2])
    #             print(f"dir_path: {dir_path}")
    #             if (request[0] == "GET"):
    #                 try:
    #                     with open(file_path, 'r') as f:
    #                         content = f.read()
    #                         length = len(content)
    #                         print(f"content: {content}; length: {length}")
    #                     response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream{ce_response}Content-Length: {length}\r\n\r\n{content}"
    #                 except Exception as e:
    #                     print(e)
    #             elif (request[0] == "POST"):
    #                 content = raw_request.splitlines()[-1]
    #                 print(f"content: {content}")
    #                 try:
    #                     with open(file_path, 'w') as f:
    #                         f.write(content)
    #                     response = "HTTP/1.1 201 Created\r\n\r\n"
    #                 except Exception as e:
    #                     print(e)
    #         print(f"response: {response}")
    #         client_conn.sendall(response.encode())
    # with ThreadPoolExecutor(max_workers=10) as pool:
    #     while True:
    #         client_conn, _ = server_socket.accept()
    #         pool.submit(handle_client, client_conn)


    # task 10 
    # from concurrent.futures import ThreadPoolExecutor
    # def handle_client(client_conn):
    #     with client_conn:
    #         raw_request = client_conn.recv(4096).decode()
    #         print(f"raw_request: {raw_request}")
    #         request = raw_request.split(" ")
    #         request_path = request[1].split("/")
    #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    #         headers = { n.split(": ")[0]: n.split(": ")[1] for n in raw_request.splitlines()[1:-1] if len(n) > 1}
    #         content_encoding = headers.get('Accept-Encoding')
    #         content_encoding = [i.strip() for i in content_encoding.split(",")] if content_encoding is not None else []
    #         print(f"content_encoding: {content_encoding}")
    #         ce_response = "\r\n"
    #         if "gzip" in content_encoding:
    #             ce_response = "\r\nContent-Encoding: gzip\r\n"
    #         if (request[0] == "GET") & (request[1] == "/"):
    #             response = "HTTP/1.1 200 OK\r\n\r\n"
    #         elif (request[0] == "GET") & (request_path[1] == "echo"):
    #             request_msg = request_path[2]
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain{ce_response}Content-Length: {len(request_msg)}\r\n\r\n{request_msg}"
    #         elif (request[0] == "GET") & (request[1] == "/user-agent"):
    #             user_agent = headers['User-Agent']
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain{ce_response}Content-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    #         elif (request_path[1] == "files"):
    #             print("args: {}".format(sys.argv))
    #             dir_path = sys.argv[2] if len(sys.argv) > 2 else ''
    #             file_path = "{}{}".format(dir_path, request_path[2])
    #             print(f"dir_path: {dir_path}")
    #             if (request[0] == "GET"):
    #                 try:
    #                     with open(file_path, 'r') as f:
    #                         content = f.read()
    #                         length = len(content)
    #                         print(f"content: {content}; length: {length}")
    #                     response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream{ce_response}Content-Length: {length}\r\n\r\n{content}"
    #                 except Exception as e:
    #                     print(e)
    #             elif (request[0] == "POST"):
    #                 content = raw_request.splitlines()[-1]
    #                 print(f"content: {content}")
    #                 try:
    #                     with open(file_path, 'w') as f:
    #                         f.write(content)
    #                     response = "HTTP/1.1 201 Created\r\n\r\n"
    #                 except Exception as e:
    #                     print(e)
    #         print(f"response: {response}")
    #         client_conn.sendall(response.encode())
    # with ThreadPoolExecutor(max_workers=10) as pool:
    #     while True:
    #         client_conn, _ = server_socket.accept()
    #         pool.submit(handle_client, client_conn)


    # task 11
    from concurrent.futures import ThreadPoolExecutor
    import gzip 

    def handle_client(client_conn):
        def encode_response(content: str, use_gzip: bool=False):
            content = content.encode()
            header = f"Content-Length: {len(content)}\r\n"
            if use_gzip:
                content = gzip.compress(content)
                header = f"Content-Encoding: gzip\r\nContent-Length: {len(content)}\r\n"
            return header, content

        with client_conn:
            raw_request = client_conn.recv(4096).decode()
            print(f"raw_request: {raw_request}")
            request = raw_request.split(" ")
            request_path = request[1].split("/")
            header = "HTTP/1.1 404 Not Found\r\n\r\n"
            response_body = b""
            headers = { n.split(": ")[0]: n.split(": ")[1] for n in raw_request.splitlines()[1:-1] if len(n) > 1}
            content_encoding = headers.get('Accept-Encoding')
            content_encoding = [i.strip() for i in content_encoding.split(",")] if content_encoding else []
            # print(f"content_encoding: {content_encoding}")
            use_gzip = True if "gzip" in content_encoding else False
            if (request[0] == "GET") & (request[1] == "/"):
                header = "HTTP/1.1 200 OK\r\n\r\n"
            elif (request[0] == "GET") & (request_path[1] == "echo"):
                header, response_body = encode_response(request_path[2], use_gzip)
                header = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n{header}\r\n"
            elif (request[0] == "GET") & (request[1] == "/user-agent"):
                header, response_body = encode_response(headers['User-Agent'], use_gzip)
                header = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n{header}\r\n"
            elif (request_path[1] == "files"):
                dir_path = sys.argv[2] if len(sys.argv) > 2 else ''
                file_path = "{}{}".format(dir_path, request_path[2])
                if (request[0] == "GET"):
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read()
                        header, response_body = encode_response(content, use_gzip)                        
                        header = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\n{header}\r\n"
                    except Exception as e:
                        print(e)
                elif (request[0] == "POST"):
                    content = raw_request.splitlines()[-1]
                    print(f"content: {content}")
                    try:
                        with open(file_path, 'w') as f:
                            f.write(content)
                        header = "HTTP/1.1 201 Created\r\n\r\n"
                    except Exception as e:
                        print(e)
            response = header.encode() + response_body
            print(f"response: {response}")
            client_conn.sendall(response)

    with ThreadPoolExecutor(max_workers=10) as pool:
        while True:
            client_conn, _ = server_socket.accept()
            pool.submit(handle_client, client_conn)

if __name__ == "__main__":
    main()
