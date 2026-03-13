import socket
import threading

HOST = '127.0.0.1'  # Dirección IP del servidor

PORT = 5000       # Puerto de escucha del servidor

def on_new_client(conn):
     while True:
         #print(f"Conectado por {addr}")
         data = conn.recv(1024)  # Recibe hasta 1024 bytes de datos
         mensaje_recibido = data.decode('utf-8')
         print(f"Servidor recibió: {mensaje_recibido}")
         respuesta = f"Servidor recibió tu mensaje: '{mensaje_recibido}'".encode('utf-8')
         conn.sendall(respuesta)  # Envía una respuesta al cliente

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))

    s.listen()  # Espera una conexión

    #print(f"Servidor escuchando en {HOST}:{PORT}")
    while True:
     conn, addr = s.accept()

     thread  = threading.Thread(target= on_new_client, args=(conn, addr))
     thread.start()
     print(f"[CONEXIONES ACTIVAS] {threading.active_count()}")

