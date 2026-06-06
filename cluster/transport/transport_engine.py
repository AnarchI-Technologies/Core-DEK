import socket
import json
import threading

class ClusterTransport:
    def __init__(self, host="127.0.0.1", port=9100):
        self.host = host
        self.port = port
        self.server = None
        self.peers = set()

    def start_listener(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        print(f"[TRANSPORT] Listening on {self.host}:{self.port}")

        while True:
            conn, addr = self.server.accept()
            threading.Thread(
                target=self.handle_connection,
                args=(conn,),
                daemon=True
            ).start()

    def handle_connection(self, conn):
        try:
            data = conn.recv(65535).decode()
            packet = json.loads(data)

            print(f"[TRANSPORT] Received packet: {packet}")

        except Exception as e:
            print(f"[TRANSPORT ERROR] {e}")

        finally:
            conn.close()

    def send_packet(self, host, port, payload):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            serialized = json.dumps(payload).encode()

            s.send(serialized)
            s.close()

            print(f"[TRANSPORT] Sent packet to {host}:{port}")

        except Exception as e:
            print(f"[TRANSPORT ERROR] {e}")
