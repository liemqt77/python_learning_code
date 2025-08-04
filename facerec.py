from deepface import DeepFace
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        cv2.putText(frame, f"Ekspresi: {emotion}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    except:
        emotion = "Tidak terdeteksi"

    cv2.imshow("Deteksi Ekspresi Wajah", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
