## repository setup

```bash
git clone https://git.codecrafters.io/9b5830ca080e860e codecrafters-http-server-python
cd codecrafters-http-server-python
```

- push empty commit 

```bash 
git commit --allow-empty -m 'test'
git push origin master
```

---------------------------------------------------
## Task 1

In this stage, you'll create a TCP server that listens on port 4221.

TCP is the underlying protocol used by HTTP servers.

```python
# app/main.py
import socket
def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept() # wait for client
```

The tester will execute your program like this:

```
$ ./your_program.sh
```

Then, the tester will try to connect to your server on port 4221. The connection must succeed for you to pass this stage.

### Notes
- To learn how HTTP works, you'll implement your server from scratch using TCP primitives instead of using Python's built-in HTTP libraries.

---------------------------------------------------
## Task 2 

In this stage, your server will respond to an HTTP request with a 200 response.

- An HTTP response is made up of three parts, each separated by a [CRLF](https://developer.mozilla.org/en-US/docs/Glossary/CRLF) (\r\n):

1. Status line.
2. Zero or more headers, each ending with a CRLF.
3. Optional response body.

In this stage, your server's response will only contain a status line. Here's the response your server must send:

```bash
HTTP/1.1 200 OK\r\n\r\n
```

Here's a breakdown of the response:
```bash 
// Status line
HTTP/1.1  // HTTP version
200       // Status code
OK        // Optional reason phrase
\r\n      // CRLF that marks the end of the status line

// Headers (empty)
\r\n      // CRLF that marks the end of the headers

// Response body (empty)
```

For more information about HTTP responses, see the [MDN Web Docs on HTTP responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages#http_responses) or the [HTTP/1.1 specification](https://datatracker.ietf.org/doc/html/rfc9112#name-message).

- The tester will execute your program like this:
```bash
$ ./your_program.sh
```

- The tester will then send an HTTP GET request to your server:
```bash
$ curl -v http://localhost:4221
```

- Your server must respond to the request with the following response:
```bash
HTTP/1.1 200 OK\r\n\r\n
```

### Notes
- You can ignore the contents of the request. We'll cover parsing requests in later stages.
- This challenge uses HTTP/1.1.
- To learn how HTTP works, you'll implement your server from scratch using TCP primitives instead of using Python's built-in HTTP libraries.

---------------------------------------------------
## Task 3

In this stage, your server will extract the URL path from an HTTP request, and respond with either a `200` or `404`, depending on the path.

### HTTP request 

- An HTTP request is made up of three parts, each separated by a CRLF (\r\n):

1. Request line.
2. Zero or more headers, each ending with a CRLF.
3. Optional request body.

- Here's an example of an HTTP request:
```bash
GET /index.html HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\nAccept: */*\r\n\r\n
```

- Here's a breakdown of the request:
```bash
// Request line
GET                          // HTTP method
/index.html                  // Request target
HTTP/1.1                     // HTTP version
\r\n                         // CRLF that marks the end of the request line

// Headers
Host: localhost:4221\r\n     // Header that specifies the server's host and port
User-Agent: curl/7.64.1\r\n  // Header that describes the client's user agent
Accept: */*\r\n              // Header that specifies which media types the client can accept
\r\n                         // CRLF that marks the end of the headers

// Request body (empty)
```

- The "request target" specifies the URL path for this request. In this example, the URL path is `/index.html`.
- Note that each header ends in a CRLF, and the entire header section also ends in a CRLF.

### Tests
- The tester will execute your program like this:
```bash
$ ./your_program.sh
```

- The tester will then send two HTTP requests to your server.
- First, the tester will send a GET request, with a random string as the path:
```bash
$ curl -v http://localhost:4221/abcdefg
```

- Your server must respond to this request with a 404 response:
```bash
HTTP/1.1 404 Not Found\r\n\r\n
```

- Then, the tester will send a `GET` request, with the path `/`:
```bash
$ curl -v http://localhost:4221
```

- Your server must respond to this request with a `200` response:
```bash
HTTP/1.1 200 OK\r\n\r\n
```

### Notes
- You can ignore the headers for now. You'll learn about parsing headers in a later stage.
- In this stage, the request target is written as a URL path. But the request target actually has [four possible formats](https://datatracker.ietf.org/doc/html/rfc9112#section-3.2). The URL path format is called the "origin form," and it's the most commonly used format. The other formats are used for more niche scenarios, like sending a request through a proxy.
- For more information about HTTP requests, see the MDN Web Docs on HTTP requests or the HTTP/1.1 specification.

---------------------------------------------------

