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
                (int)(self.center[0] + self.width/2 + 0.5),
                (int)(self.center[1] + self.width/2 + 0.5))

    def __repr__(self):
        return "Shape()"
    def __str__(self):
        return "Shape: " + str(self.shapeType) +\
        ", Height: " + str(self.height) +\
        ", Width: " + str(self.width) +\
        ", Center: " + str(self.center)

    def Overlap(self,shape):
        # https://gamedev.stackexchange.com/questions/586/what-is-the-fastest-way-to-work-out-2d-bounding-box-intersection
        return ((abs(self.center[0] - shape.center[0]) < (self.width + shape.width)/2) and
        (abs(self.center[1] - shape.center[1]) < (self.width + shape.width)/2))

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

class ShapeInfo:
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

        imageInfo.height = random.randint(
            imageInfo.heightInterval[0],
            imageInfo.heightInterval[1])

        img.fill(imageInfo.height)

        shapeList = list()
        for i in range(0, shapeInfo.shapes):
            
            shape = None
            while True:
                shape = ShapeGenerator.GenerateShape(
                imageInfo,
                shapeInfo)

                if(shape.valid(shapeList)):
                    break

            shapeList.append(shape)

            shape.draw(img, imageInfo.height)

        return img, shapeList

    @staticmethod
    def GenerateSamples(
        imageInfo,
        shapeInfo,
        numberOfSamples):


        samples = np.zeros((numberOfSamples, imageInfo.size[0], imageInfo.size[1]), np.uint8)
        labels = np.zeros(numberOfSamples, np.uint8)

        for x in range(0, numberOfSamples):
            img, shapeList = ShapeGenerator.GenerateImageWithShapes(imageInfo, shapeInfo)
            samples[x,:,:] = img
            labels[x] = shapeList[0].shapeType.value
        return samples, labels

    @staticmethod
    def GenerateDataSet(
        imageInfo,
        shapeInfo,
        nmbTrainingSamples,
        nmbTestSamples):

        train_images, train_labels = ShapeGenerator.GenerateSamples(imageInfo, shapeInfo, nmbTrainingSamples)
        test_images, test_labels = ShapeGenerator.GenerateSamples(imageInfo, shapeInfo, nmbTestSamples)
        return (train_images, train_labels), (test_images, test_labels)
