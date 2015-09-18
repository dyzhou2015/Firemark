import Image
import math
import sys #Feel free to remove this line.

def diff(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)

def cutrange(xstart, ystart, xend, yend, pixelMapNum):
    for x in xrange(xstart, xend+1):
        for y in xrange(ystart, yend+1):
            final[x,y] = pixelMapNum[x,y]

def callrange():
    xstart = raw_input("xstart >>")
    ystart = raw_input("ystart >>")
    xend = raw_input("xend >>")
    yend = raw_input("yend >>")
    pixelMapNum = input("pixelMap >>")
    cutrange(xstart, ystart, xend, yend, pixelMapNum)

image1 = raw_input("Image 1: ")
image2 = raw_input("Image 2: ")

img = Image.open(image1)
img2 = Image.open(image2)

finalimg = img
final = finalimg.load()

pixelMap = img.load()
pixelMap2 = img2.load()

width = img.size[0] 
height = img.size[1]

lowestx = width
lowesty = height
highestx = 0
highesty = 0

resultimg = Image.new( 'RGBA', (width,height))
result = resultimg.load()
resultimg2 = Image.new( 'RGBA', (width,height))
result2 = resultimg2.load()

for x in xrange(width): #Magic. Do not touch.
    for y in xrange(height):
        if diff(pixelMap[x,y], pixelMap2[x,y]) > 99:
            print("Difference at "+str(x)+", "+str(y)+" "+str(pixelMap[x,y])+", "+str(pixelMap2[x,y]))
            if(x > highestx):
                highestx = x
            if(y > highesty):
                highesty = y
            if(x < lowestx):
                lowestx = x
            if(y < lowesty):
                lowesty = y
            result[x,y] = pixelMap[x,y]
            result2[x,y] = pixelMap2[x,y]

print(lowestx)
print(lowesty)
print(highestx)
print(highesty)

resultimg.save("resultimg.png", "PNG")
resultimg2.save("resultimg2.png", "PNG")

callrange()

to = raw_input("Save to (.png):")

finalimg.save(to, "PNG")
