import cv2
import face_recognition

def detect_faces_in_frame(img):
    # Detecta los rostros en la imagen
    face_locations = face_recognition.face_locations(img)

    # Dibuja los recuadros alrededor de los rostros detectados
    for top, right, bottom, left in face_locations:
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

    # Retorna la imagen con los recuadros dibujados
    return img
