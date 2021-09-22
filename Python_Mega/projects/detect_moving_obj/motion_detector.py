from typing import Counter
import cv2


def motion_detector():
  """Live motion detector app"""
  
  # capture camera frames
  video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

  # detecting frames
  first_frame = None
  
  while True:
    
    check, frame = video.read()
    
    # convert image to grey
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # blur the grey image:
    grey = cv2.GaussianBlur(grey, (21, 21), 0)
    
    if first_frame is None:
      first_frame= grey
      continue

    delta_frame = cv2.absdiff(first_frame, grey)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(
      thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
      )
    
    for contour in cnts:
      if cv2.contourArea(Counter) < 1000:
        continue
      x, y, w, h = cv2.boundingRect(contour)
      cv2.rectangle(frame, (x, y), (x+w), (y+h), (0, 255, 255), 2)

    # show live feed:
    cv2.imshow("grey frame", grey)
    cv2.imshow("delta frame", delta_frame)
    cv2.imshow("Threshold frame", thresh_frame)


    abort = cv2.waitKey(1)
    if abort == ord(" "):
      break
      
  
  video.release()
  cv2.destroyAllWindows()
  
  

if __name__ == "__main__":
  print(motion_detector())


  
  
  
  