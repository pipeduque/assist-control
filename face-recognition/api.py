from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import face_recognition
import numpy as np

app = Flask(__name__)
CORS(app)


# Cargar imágenes de los empleados y sus nombres
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


@app.route("/recognize", methods=["POST"])
def recognize():
    file = request.files["image"]
    image = face_recognition.load_image_file(file)
    face_encodings = face_recognition.face_encodings(image)
    results = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconocido"

        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding
        )
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        results.append(name)

    return jsonify(results)


if __name__ == "__main__":
    app.run(port=5000)
