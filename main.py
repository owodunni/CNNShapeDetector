from ShapeGenerator import ShapeGenerator, ImageInfo, ShapeInfo

import numpy as np
import cv2
import tensorflow as tf

imageInfo = ImageInfo(
                size = (64,64),
                heightInterval = (40, 80))
shapeInfo = ShapeInfo(
                shapes = 1,
                widthInterval = (2, 10), 
                heightInterval = (10, 150))

#X = tf.placeholder(
#    tf.float32,
#    [None, imageInfo.size[1], imageInfo.size[0], 1])
#Y = tf.placeholder(tf.float32, [None, 2])

#print ("X = " + str(X))
#print ("Y = " + str(Y))

#ShapeDict = ShapeGenerator.GenerateImageWithShapes(imageInfo, shapeInfo)

#print(ShapeDict["ShapeList"][0])

#cv2.imshow('image',ShapeDict["Image"])
#cv2.waitKey(0)
#cv2.destroyAllWindows()