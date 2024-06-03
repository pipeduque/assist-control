import cv2
import face_recognition
import os
import numpy as np

# Cargar las imágenes de los empleados y sus nombres
known_face_encodings = []
known_face_names = []

for filename in os.listdir(
    "/Users/jduque@truora.com/Documents/Ucaldas/aut/face-recognition/know_faces"
):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = face_recognition.load_image_file(
            os.path.join(
                "/Users/jduque@truora.com/Documents/Ucaldas/aut/face-recognition/know_faces",
                filename,
            )
        )
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(filename.split(".")[0])

# Iniciar la cámara
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: No se puede acceder a la cámara.")
    exit()

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: No se puede capturar la imagen.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(
        face_locations, face_encodings
    ):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconocido"

        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding
        )
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(
            frame,
            name,
            (left + 6, bottom - 6),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (0, 0, 255),
            1,
        )

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
