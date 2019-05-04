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
        self.p1 = (
                (int)(self.center[0] - self.width/2),
                (int)(self.center[1] - self.width/2))
        self.p2 = (
                (int)(self.center[0] + self.width/2),
                (int)(self.center[1] + self.width/2))

    def __repr__(self):
        return "Shape()"
    def __str__(self):
        return "Shape: " + str(self.shapeType) +\
        ", Height: " + str(self.height) +\
        ", Width: " + str(self.width) +\
        ", Center: " + str(self.center)

    def Overlap(self,shape):
        for x in range(0,2):
            if(shape.p2[x] < self.p1[x] or
            shape.p1[x] > self.p2[x]):
                return False
        return True

    def valid(
        self,
        shapeList):
        for shape in shapeList:
            if(shape.Overlap(self)):
                return False
        return True
    
    def draw(
        self,
        img,
        imgHeight):

        shapeColor = self.height + imgHeight

        if(ShapeType.rectangle == self.shapeType):
            cv2.rectangle(
                img,
                self.p1,
                self.p2,
                (shapeColor, shapeColor, shapeColor),
                -1)
        else:
            cv2.circle(
                img,
                self.center,
                int(self.width/2),
                (shapeColor, shapeColor, shapeColor),
                -1)
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
        self.height = random.randint(
            heightInterval[0],
            heightInterval[1])

class ShapeGenerator:

    @staticmethod
    def GenerateShape(
        imageInfo,
        shapeInfo):
        shapeType = random.choice(list(ShapeType))

        shapeWidth = random.randint(
            shapeInfo.widthInterval[0],
            shapeInfo.widthInterval[1])

        shapeHeight = random.randint(
            shapeInfo.heightInterval[0],
            shapeInfo.heightInterval[1])

            # Limit shape width so that shapes can not be outside image
        shapeCenter = (
            random.randint(
                (int)(shapeWidth/2),
                imageInfo.size[0] - (int)(shapeWidth/2)),
            random.randint(
                (int)(shapeWidth/2),
                imageInfo.size[1] - (int)(shapeWidth/2)))

        shape = Shape(
            shapeType,
            shapeHeight,
            shapeWidth,
            shapeCenter)
        return shape

    @staticmethod
    def GenerateImageWithShapes(
        imageInfo,
        shapeInfo):
        # Create a black image
        img = np.zeros(imageInfo.size, np.uint8)

        img.fill(imageInfo.height)

        shapeList = list()
        for i in range(0, shapeInfo.shapes):
            
            shape = None
            while True:
                shape = ShapeGenerator.GenerateShape(
                imageInfo,
                shapeInfo)

                print(shape)
                if(shape.valid(shapeList)):
                    print("Shape is valid breaking loop")
                    break
                else:
                    print("Invalid shape generating new")

            shapeList.append(shape)

            shape.draw(img, imageInfo.height)

        return {
            "Image": img,
            "ShapeList": shapeList
        }

ShapeDict = ShapeGenerator.GenerateImageWithShapes(
    ImageInfo(
        size = (600,600),
        heightInterval = (40, 80)),
    Shapeinfo(
        shapes = 50,
        widthInterval = (10, 50), 
        heightInterval = (10, 150)))

cv2.imshow('image',ShapeDict["Image"])
cv2.waitKey(0)
cv2.destroyAllWindows()