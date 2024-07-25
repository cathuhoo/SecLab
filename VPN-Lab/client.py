import socket
import ssl
import threading

class server_ssl:
    def build_listen(self):
        KEY_FILE = "server-key.pem"
        CERT_FILE = "server-cert.pem"
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        
        # 加载服务器证书和私钥
        context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
        context.verify_mode = ssl.CERT_NONE  # 如果需要单向认证，设置为CERT_NONE

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            with context.wrap_socket(sock, server_side=True) as ssock:
                ssock.bind(('0.0.0.0', 10028))
                ssock.listen(5)
                print("Server is listening for connections...")
                while True:
                    client_socket, addr = ssock.accept()
                    print(f"Accepted connection from {addr}")
                    client_thread = threading.Thread(target=self.handle_client, args=(client_socket, addr))
                    client_thread.start()

    def handle_client(self, client_socket, addr):
        try:
            while True:
                # 读取来自客户端的消息
                msg = client_socket.recv(1024).decode("utf-8")
                if not msg:
                    break
                
                print(f"Received message from client {addr}: {msg}")
                
                # 发送回执
                response = f"Received: {msg}".encode("utf-8")
                client_socket.send(response)

        except Exception as e:  # 捕获正确的异常类型
            print(f"Error: {str(e)}")
        finally:
            client_socket.close()
            print("Connection closed")

if __name__ == "__main__":
    server = server_ssl()
    server.build_listen()
