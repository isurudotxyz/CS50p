import sys

from PIL import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)

# auto close by saving
# while saving it forma the file as a unique file
# meaning that it will loop through all of them

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
