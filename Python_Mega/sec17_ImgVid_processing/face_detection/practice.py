import cv2
import matplotlib.pyplot as plt

# cascade path:
haarcascade = "/Users/USER10/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/"

def face_detect():

  # setting up cascades path:
  casc_path = f"{haarcascade}haarcascade_frontalface_default.xml"
  eye_path = f"{haarcascade}haarcascade_eye.xml"
  smile_path = f"{haarcascade}haarcascade_smile.xml"
  
  # creating cascading classifier objects:
  face_cascade = cv2.CascadeClassifier(casc_path)
  eye_cascade = cv2.CascadeClassifier(eye_path)
  smile_cascade = cv2.CascadeClassifier(smile_path)

  # load image
  img = cv2.imread("./files/photo.jpg")


  
  # detect faces and draw rectangles around them
  faces = face_cascade.detectMultiScale(
    img,
    scaleFactor=1.3,
    minNeighbors=5,
    flags=cv2.CASCADE_SCALE_IMAGE,
  )

  # extract coords for each face
  for (x, y, w, h) in faces:
    # draw a rectangle around each face
    cv2.rectangle(
      img=img, 
      pt1=(x, y),
      pt2=(x+w, y+h),
      color=(0, 255, 255),
      thickness=2
      )

  # show image and let user manually closes it
  # cv2.imshow("Father & Son", rectangles)

  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

  # show results using matplot
  plt.figure(figsize=(12, 8))
  plt.imshow(img, cmap="gray")
  plt.show()

  return "Thank you."


if __name__ == "__main__":
  print(face_detect())