from flask import Flask, render_template
from flask_socketio import SocketIO
import numpy as np
import cv2
import base64
import detect_faces_script

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    # Mensaje al cargar la página principal y establecer la conexión WebSocket
    print("Cargando la página principal y esperando conexiones...")
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # Mensaje cuando un cliente se conecta
    print("Un cliente se ha conectado.")

@socketio.on('disconnect')
def handle_disconnect():
    # Mensaje cuando un cliente se desconecta
    print("Un cliente se ha desconectado.")

@socketio.on('frame')
def handle_frame(data):
    # Mensaje al recibir un cuadro de video
    print("Recibiendo cuadro de video para procesamiento...")

    # Decodificar y procesar el cuadro
    frame = data['image']
    frame = base64.b64decode(frame)
    nparr = np.frombuffer(frame, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Llamar al script de detección de rostros (modifica esta función según necesidad)
    detect_faces_script.detect_faces_in_frame(img)

    # Mensaje después de procesar el cuadro
    print("Cuadro procesado. Detectando rostros...")

    # Si necesitas enviar información de vuelta al cliente
    # emit('response', {'data': 'Respuesta procesada'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
