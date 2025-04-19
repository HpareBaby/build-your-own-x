## Task 2
- To pass this stage, you'll need to (a) wait for a client connection and (b) send a PONG response.
- To wait for a client connection, you can use the [`socket.accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept) method, which blocks until a client connects. Once connected, it returns a [`Socket`](https://docs.python.org/3/library/socket.html#socket-objects) object representing the client connection:
```python
connection, _ = server_socket.accept()
```
- `accept()` also returns the client’s address which we ignore with `_`.
- After the connection is established, you can send a PONG message using [`socket.sendall()`](https://docs.python.org/3/library/socket.html#socket.socket.sendall), which accepts a [bytes-like object](https://docs.python.org/3/library/socket.html#socket.socket.sendall):
```python
connection.sendall(b"+PONG\r\n")
```
- `+PONG\r\n` is the string "PONG" encoded as a [simple string](https://redis.io/docs/latest/develop/reference/protocol-spec/#simple-strings) using the Redis protocol.


----------------------------------------------------

