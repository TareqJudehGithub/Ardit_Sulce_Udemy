import cv2


haarcascade = "/Users/USER10/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/"

cascPath = f"{haarcascade}haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(200, 200),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            img=frame, 
            pt1=(x, y), 
            pt2=(x+w, y+h),
            color=(255, 0, 0), 
            thickness= 3
            )

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord(' '):
      break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()