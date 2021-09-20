import glob
import os
import cv2


def resize_imgs():
  """Multi mage processing using openCV"""

  # assing source and destination folders
  src_folder = "./files/sample_images/"
  dst_folder = "./files/edited_images/"
  
  # iterate over all files in the source folder, and read them using cv2
  for file in os.listdir(src_folder):

    image = cv2.imread(filename=f"{src_folder}{file}", flags=1)

    # split file extension from it's name
    split_ext = os.path.splitext(file)

   
    # downscale all images 50%

    # setting up images new diminsions
    scale_percent = 50
    img_dim = image.shape
    img_width = int(img_dim[1] * scale_percent/100)
    img_height = int(img_dim[0] * 125/100)

    # downscale all images
    resize_imgs = cv2.resize(src=image, dsize=(img_width, img_height))

    # show downscaled images to user 
    cv2.imshow(file, resize_imgs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # check if the destination folder exists, if not then create it
    if not os.path.exists(dst_folder):
      os.makedirs(dst_folder)

    else:
      # save new images as png file format
      if not file.endswith(".png"):
        cv2.imwrite(f"{dst_folder}{split_ext[0]}.png", resize_imgs)
      else:
        cv2.imwrite(f"{dst_folder}{file}", resize_imgs)
    
  return os.listdir(dst_folder)


if __name__ == "__main__":
  print(resize_imgs())
