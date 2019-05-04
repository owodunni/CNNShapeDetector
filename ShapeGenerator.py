import numpy as np
import cv2
from enum import Enum
import random
class ShapeType(Enum):
    rectangle = 0
    circle = 1

class Shape:
    def __init__(
        self,
        shapeType,
        height,
        width,
        center):
        self.shapeType = shapeType
        self.height = height
        self.width = width
        self.center = center

    def __repr__(self):
        return "Shape()"
    def __str__(self):
        return "Shape: " + str(self.shapeType) +\
        " ,Height: " + str(self.height) +\
        " ,Width: " + str(self.width) +\
        " , Center: " + str(self.center)
    
    def valid(
        self,
        shapeList):
        return True
    
    def draw(
        self,
        img,
        imgHeight):

        if(ShapeType.rectangle == self.shapeType):
            p1 = (
                self.center[0] - self.width/2,
                self.center[1] - self.width/2)
            p2 = (
                self.center[0] + self.width/2,
                self.center[1] + self.width/2)
            cv2.rectangle(
                img,
                p1,
                p2,
                self.height + imgHeight,
                3)
        else:
            cv2.circle(img,
            self.center,
            self.width/2,
            self.height + imgHeight, -1)
        return img

class Shapeinfo:
    def __init__(
        self,
        shapes,
        widthInterval,
        heightInterval):
        self.shapes = shapes
        self.widthInterval = widthInterval
        self.heightInterval = heightInterval

class ImageInfo:
    def __init__(
        self,
        size,
        heightInterval):
        self.size = size
        self.heightInterval = heightInterval

class ShapeGenerator:

    @staticmethod
    def GenerateImageWithShapes(
        imageInfo,
        shapeInfo):
        # Create a black image
        img = np.zeros(imageInfo.size, np.uint8)

        imgHeight = random.randint(
            imageInfo.heightInterval[0],
            imageInfo.heightInterval[1])

        print("Image height: " + str(imgHeight))

        img.fill(imgHeight)

        for i in range(0, shapeInfo.shapes):
            
            shapeType = random.choice(list(ShapeType))

            shapeWidth = random.randint(
                shapeInfo.widthInterval[0],
                shapeInfo.widthInterval[1])

            shapeHeight = random.randint(
                shapeInfo.heightInterval[0],
                shapeInfo.heightInterval[1])

            shapeCenter = (
                random.randint(
                    0,
                    imageInfo.size[0]),
                random.randint(
                    0,
                    imageInfo.size[1]))
            shape = Shape(
                shapeType,
                shapeHeight,
                shapeWidth,
                shapeCenter)
            
            print(shape)

            #shape.draw(img, imgHeight)

        return img

img = ShapeGenerator.GenerateImageWithShapes(
    ImageInfo(
        size = (200,200),
        heightInterval = (40, 80)),
    Shapeinfo(
        shapes = 5,
        widthInterval = (10, 50), 
        heightInterval = (10, 20)))

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()