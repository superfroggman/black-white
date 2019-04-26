import pygame
import sys

pygame.init()
 

print sys.argv[1]
# my stuff
image = pygame.image.load(sys.argv[1])

for x in xrange(0, image.get_rect().size[0]):
    print (x+1)
    print ("/")
    print (image.get_rect().size[0])
    print ("-----------")
    for y in xrange(0, image.get_rect().size[1]):
        pixel = image.get_at((x, y))
        color = (pixel[0]+pixel[1]+pixel[2])/3
        image.set_at((x,y), (color,color,color))
print ("DONE!")

pygame.image.save(image, sys.argv[2])