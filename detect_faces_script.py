# Requiere la instalación de la biblioteca: pip install face_recognition
import face_recognition
import cv2

def detect_faces(image_path):
    # Cargar la imagen y encontrar las ubicaciones de los rostros
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # Cargar la imagen con OpenCV para dibujar los cuadros
    image_cv = cv2.imread(image_path)

    # Dibujar los cuadros alrededor de cada rostro
    for top, right, bottom, left in face_locations:
        cv2.rectangle(image_cv, (left, top), (right, bottom), (0, 0, 255), 2)

    # Guardar la imagen
    cv2.imwrite('output.jpg', image_cv)
