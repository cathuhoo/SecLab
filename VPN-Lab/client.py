#!/usr/bin/evn python3

import socket
import ssl
import time

class client_ssl:
    def send_hello(self):
        CA_FILE = "ca-cert.pem"
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False  # 如果不需要检查主机名，可以设置为False
        context.load_verify_locations(CA_FILE)  # 加载CA证书
        context.verify_mode = ssl.CERT_REQUIRED  # 需要进行证书验证

        with socket.socket() as sock:
            with context.wrap_socket(sock, server_side=False) as ssock:
                ssock.connect(('172.16.1.30', 10028))
                try:
                    while True:
                        msg = input("Enter a message to send (or 'quit' to exit): ")
                        if msg.lower() == 'quit':
                            break
                        ssock.send(msg.encode("utf-8"))
                        response = ssock.recv(1024).decode("utf-8")
                        print(f"Received message from the server: {response}")
                        time.sleep(1)  # 每发送一次消息后等待1秒
                except Exception as e:
                    print(f"Error: {str(e)}")

if __name__ == "__main__":
    client = client_ssl()
    client.send_hello()
