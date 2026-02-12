import cv2
import os

# Directory to save face images
save_dir = "dataset"
os.makedirs(save_dir, exist_ok=True)

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

captured = False
photo_count = 0

print(" Automatically captures a full photo once when a *real face* is detected. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Improve detection by converting to grayscale and equalizing brightness
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Detect faces with stricter parameters
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # smaller step between scales = more accurate
        minNeighbors=7,   # higher = fewer false detections
        minSize=(100, 100)  # ignore tiny areas (like switchboards)
    )

    # Draw rectangle around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Capture full frame when faces are detected
    if len(faces) > 0 and not captured:
        photo_filename = os.path.join(save_dir, f"photo_{photo_count}.jpg")
        cv2.imwrite(photo_filename, frame)
        print(f" Saved full photo: {photo_filename}")
        photo_count += 1

        captured = True
        captured_frame = frame.copy()
        print(" Face detected and photo captured successfully! Showing image...")

        # Show captured frame for 2 seconds
        cv2.imshow("Captured Frame", captured_frame)
        cv2.waitKey(2000)
        cv2.destroyWindow("Captured Frame")

    cv2.imshow("Face Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"\nTotal photos saved: {photo_count}")
print(f"Images saved in: {save_dir}")

