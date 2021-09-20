import cv2 as cv


galaxy = cv.imread("./files/galaxy.jpg", flags=0)

img_dim = galaxy.shape
print(f"Original dim: {img_dim}")   # current size = (1485, 990)

# downscale img by 50%
scale_size = 50

width = int(img_dim[1] * (scale_size/ 100))
height = int(img_dim[0] * (scale_size/ 100))


# we can resize the image before showing it, using .resize() method
resized_galaxy = cv.resize(src=galaxy, dsize=(width, height))
print(f"New dim: {resized_galaxy.shape}")

# show image on screen:
cv.imshow("./files/galaxy.jpg", resized_galaxy)

# save the new resized image in a new file:
cv.imwrite(filename="./files/galaxy_edited.png", img=resized_galaxy)

# 0 param means the user will manually closes the images.
cv.waitKey(5000)    # 5 seconds
cv.destroyAllWindows()
