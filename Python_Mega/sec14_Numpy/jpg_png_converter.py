from PIL import Image
import sys, os



new_img = Image.open("./jpg_folder/bulbasaur.jpg")



# grab first and second  argument
jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

print(jpg_folder, png_folder)


# check if new/existed folder
if not os.path.exists(png_folder):
  os.makedirs(png_folder)

else:
  # create the folder
  print("Folder exists. Thank you.")


# iterate over files folder
for filename in os.listdir(jpg_folder):
  # access to image files inside jpg_folder
  img = Image.open(f"{jpg_folder}/{filename}")
  
  # split the file name from it's extension. .split() creates a tuple
  # of two indexes 0 and 1, where 0 is the filename, and 1 is the .ext
  
  split_ext = os.path.splitext(filename)[0]
  
  # convert the filenames as png, and save them in the new folder
  img.save(f"{png_folder}/{split_ext}.png", "png")

# display all files inside the png_folder  
print(os.listdir(path=png_folder))
# convert jpg to png

# save ur work
