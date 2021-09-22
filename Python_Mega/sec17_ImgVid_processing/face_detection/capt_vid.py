"""
Capturing screen shots using live camera with Python
"""
import cv2, time

# capture video (screenshot) with cv2

video = cv2.VideoCapture(0) # 0 for cam1

check, frame = video.read()
print(check, end="\n\n")    # check returns a boolean if the cam capture is working.

print("frame")
print(frame)
time.sleep(1)

# convert captured image to grayscale
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# show window
cv2.imshow("Vid Capture", grey)

# close vid window after displaying
cv2.waitKey(0)
cv2.destroyAllWindows()

# access the captured object
video.release()

