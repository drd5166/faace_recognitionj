from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import cv2
import mysql.connector
from PIL import Image
import io

app = FastAPI()

# Load once at startup
face_cascade = cv2.CascadeClassifier("../haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("../classifier.xml")

def get_name_by_id(user_id: int) -> str:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Authorized_user"
    )
    cursor = db.cursor()
    cursor.execute("SELECT Name FROM my_table WHERE id=%s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    db.close()
    if row:
        return row[0]
    else:
        return "UNKNOWN"

@app.post("/detect-face/")
async def detect_face(file: UploadFile = File(...)):
    # Read image bytes into OpenCV
    contents = await file.read()
    pil_img = Image.open(io.BytesIO(contents)).convert("RGB")
    np_img = np.array(pil_img)[:, :, ::-1]  # RGB → BGR

    gray = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    if len(faces) == 0:
        raise HTTPException(status_code=404, detail="No face detected")

    # For simplicity, take the first detected face
    x, y, w, h = faces[0]
    face_roi = gray[y:y+h, x:x+w]

    # Predict
    user_id, conf = recognizer.predict(face_roi)
    confidence = int(100 * (1 - conf / 300))
    name = get_name_by_id(user_id) if confidence > 74 else "UNKNOWN"

    return JSONResponse({"name": name, "confidence": confidence})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
