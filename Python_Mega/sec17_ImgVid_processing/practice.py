import cv2


galaxy_img = cv2.imread("./files/galaxy.jpg", cv2.IMREAD_GRAYSCALE)

# img diminsions:
print(f"img original diminsions: {galaxy_img.shape}")

# resize image: downscale it by 60%
scale_percent = 60
width = int(galaxy_img.shape[1] * scale_percent/100)

height = int(galaxy_img.shape[0] * scale_percent/100)

dim = (width, height)

galaxy_new_size = cv2.resize(src=galaxy_img, dsize=dim, interpolation=cv2.INTER_AREA)

print(f"img new diminsions: {galaxy_new_size.shape}")

# show img for 5 seconds then automatically close it
cv2.imshow("./files/galaxy.jpg", galaxy_new_size)
cv2.waitKey(5000)
cv2.destroyAllWindows()

print("Array Type: {}".format(galaxy_img.ndim))
print(dim)

 # =======================================================