import cv2


def analyze_video(video_path: str):
    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier("resource/haarcascade_frontalface_default.xml")

    # Open the video file
    video = cv2.VideoCapture(video_path)

    while True:
        # Read the next frame from the video
        ret, frame = video.read()

        # Check if the frame was successfully read
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with face detections
        cv2.imshow('Face Detection', frame)

        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close the display window
    video.release()
    cv2.destroyAllWindows()
