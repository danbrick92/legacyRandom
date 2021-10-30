# This is my own library to mess around with pictures

from PIL import Image
import random
import math

BLACK = (0,0,0)
WHITE = (255,255,255)
IMAGE_LOCATION = r'/Users/danbricknerjr/Documents/test.jpg'

# Creates greyscale by using the average of r,g,b
def greyscale(image,pixels):
    for k in range(0,image.size[0]):
        for i in range(0, image.size[1]):
            average = (pixels[k, i][0] + pixels[k, i][1] + pixels[k, i][2]) / 3
            pixels[k, i] = (average,average,average)
    return image

# Generates grain using random integers mixed with original pixels
def grain(image,pixels):
    for k in range(0,image.size[0]):
        for i in range(0, image.size[1]):
            ran1 = random.randint(0, 255)
            ran2 = random.randint(0, 255)
            ran3 = random.randint(0, 255)
            final1 = (ran1 + pixels[k,i][0]) / 2
            final2 = (ran2 + pixels[k,i][1] )/ 2
            final3 = (ran3 + pixels[k,i][2]) / 2
            pixels[k, i] = (final1,final2,final3)
    return image

# Swaps the r,g,b values to g,b,r
def swapColors(image,pixels):
    for k in range(0,image.size[0]):
        for i in range(0, image.size[1]):
            pixels[k, i] = (pixels[k, i][1], pixels[k, i][2], pixels[k, i][0])
    return image

# Inverts the image by -255 and then getting the abs value
def invert(image,pixels):
    for k in range(0,image.size[0]):
        for i in range(0, image.size[1]):
            inv1 = abs(pixels[k, i][0] - 255)
            inv2 = abs(pixels[k, i][1] - 255)
            inv3 = abs(pixels[k, i][2] - 255)
            pixels[k, i] = (inv1,inv2,inv3)
    return image

# 1/4 of original image size (1/2 height, 1/2 width) - taken by average of four squares, top left centric
def compress(image,pixels):
    newImage = Image.new('RGB',(image.size[0]/2,image.size[1]/2))
    newPixels = newImage.load()
    pixelTracker = generateTwoDArray(image.size[1],image.size[0],'False')
    for k in range(0,image.size[0]-1):
        for i in range(0, image.size[1]-1):
            if pixelTracker[i][k] == 'False':
                r = (pixels[k, i][0] + pixels[k+1, i][0] + pixels[k, i+1][0] + pixels[k+1, i+1][0])/4
                g = (pixels[k, i][1] + pixels[k + 1, i][1] + pixels[k, i + 1][1] + pixels[k + 1, i + 1][1]) / 4
                b = (pixels[k, i][2] + pixels[k + 1, i][2] + pixels[k, i + 1][2] + pixels[k + 1, i + 1][2]) / 4
                newPixels[k/2, i/2] = (r,g,b)
                pixelTracker[i][k],pixelTracker[i+1][k],pixelTracker[i][k+1],pixelTracker[i+1][k+1] = 'True'
    return newImage

# Gets the derivative in both directions (gradient) and then calculates the magnitude
def edgeDetect(image,pixels):
    newImage = Image.new('RGB', (image.size[0], image.size[1]))
    newPixels = newImage.load()
    #pixelTracker = generateTwoDArray(image.size[1], image.size[0], 0)
    for k in range(1, image.size[0] - 1):
        for i in range(1, image.size[1] - 1):
            avgLeft = (pixels[k-1, i][0] + pixels[k-1, i][1] + pixels[k-1, i][2]) / 3
            avgRight = (pixels[k+1, i][0] + pixels[k+1, i][1] + pixels[k+1, i][2]) / 3
            avgUp = (pixels[k, i-1][0] + pixels[k, i-1][1] + pixels[k, i-1][2]) / 3
            avgDown = (pixels[k, i+1][0] + pixels[k, i+1][1] + pixels[k, i+1][2]) / 3
            derivativeX = avgRight - avgLeft
            derivativeY = avgDown - avgUp
            magnitude = int(math.sqrt((abs(derivativeX)*abs(derivativeX)) + (abs(derivativeY)+abs(derivativeY))))
            newPixels[k,i] = (magnitude,magnitude,magnitude)
    return newImage

# Generates a two dimensional array and fills it with the inputted value
def generateTwoDArray(rows,columns,defaultValue):
    twoD = []
    for i in range(0,rows):
        new = []
        for j in range(0,columns):
            new.append(defaultValue)
        twoD.append(new)
    return twoD

def main():
    image = Image.open(IMAGE_LOCATION)
    pixels= image.load()
    #greyscale(image)
    #grain(image)
    #swapColors(image)
    #invert(image,pixels)
    #newImage = compress(image,pixels)
    newImage = edgeDetect(image,pixels)
    newImage.show()
    #image.show()

if __name__ == "__main__":
    main()