import cv2

# create face cascade classifier object
face_cascade = cv2.CascadeClassifier("./files/haarcascade_frontalface_default.xml")

# load image
img = cv2.imread("./files/photo.jpg")

# convert to grey colors
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search for cascade classifier object (search for faces) and return its coords
faces = face_cascade.detectMultiScale(
    img, 
    scaleFactor=1.05,
    minNeighbors=5
   )

# extract all coords as new variables

for x, y, w, h in faces:
  face_img = cv2.rectangle(
    img=img, 
    pt1=(x, y), 
    pt2=(x+w, y+h), 
    thickness=2, 
    color=(0, 250, 0)  #(blue, green, red)
    )



# convert image to 
cv2.imshow("Face Detect", face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


