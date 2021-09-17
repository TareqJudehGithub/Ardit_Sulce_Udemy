"""
openCV
- openCV lib is used for image processing in Python.
- openCV creates arrays from images.
- installation
$ pip install opencv-python
$ pip install opencv-python-headless   
 
- reading img using cv2
  img = cv2.imread("filename", 0)
    0 parameter reads the image in grayscale
    1 parameter reads the image in RGP (which is the default parameter)

- creating new images from array
  new_img = cv2.imwrite(filename="/filepath", img=cv2.imread("filepath", 0))

"""

import cv2
import numpy

print("")
print("convert image => array")
# read image, and convert image into an array
img_to_arr = cv2.imread(filename="./images/smallgray.png", flags=0)

print(img_to_arr)


print("")
print("convert array into an image")
arr_to_img = cv2.imwrite(filename="./images/image_01.png", img=img_to_arr)


print("")
print("iterating over an array")
for i in img_to_arr:
  print(i)

print("")
print("iterating over array columns")
for i in img_to_arr.T:
  print(i)



print("")
print("iterating over array value by value")
for i in img_to_arr.flat:
  print(i)

print("")
# stocking(combining) numpy arrays
print("stack two or more numpy arrays horizontally")
# stack two or more numpy arrays horizontally
# arrays must all have the same number of diminsions in order to stack them.
hor_arr = numpy.hstack(tup=(img_to_arr, img_to_arr))
print(hor_arr)

print("")
print("stack two or more numpy arrays vertically")

vert_arr = numpy.vstack(tup=(img_to_arr, img_to_arr))
print(vert_arr)

print("")
print("split arrays horizontally")
split_array_hor = numpy.hsplit(ary=hor_arr, indices_or_sections=2)
print(split_array_hor)
print(len(split_array_hor))   # >>> 2

# like the case in string.split(), .hsplit() and .vsplit() produce
# lists, which is subject to slicing and indexing.

print("")
print("split arrays vertically")
split_arr_vert = numpy.vsplit(ary=vert_arr, indices_or_sections=2)
print(split_arr_vert)  # >>> 2
print("")
print(split_arr_vert[0])
print("")
print(split_arr_vert[1])




