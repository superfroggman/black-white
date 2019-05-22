import sys
from PIL import Image
import numpy as np

img = Image.open(sys.argv[1])
rgb_im = img.convert('RGB')
pixels = img.load() # Create the pixel map
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        r, g, b = rgb_im.getpixel((i, j))
        total = int((r+g+b)/3)
        pixels[i,j] = (total,total,total)

img.show()
img.save(sys.argv[2])
print ("DONE!")
