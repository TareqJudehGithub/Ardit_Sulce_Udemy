import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cv2.CAP_DSHOW should prevent [ WARN:0] from appearing while capturing.
while True:
  # capture campera frames
  check, frame = video.read()
  print(check)
  
  # show camera live feed
  cv2.imshow("Live Cam", frame)
  
  # manually close camera window
  key = cv2.waitKey(1)
  if key == ord("\r"):
    break

# start live camera
video.release()
cv2.destroyAllWindows()


