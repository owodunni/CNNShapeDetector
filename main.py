#!/usr/bin/env python3
from ShapeGenerator import ShapeGenerator, ImageInfo, ShapeInfo

import numpy as np
import cv2
import tensorflow as tf

imageInfo = ImageInfo(
                size = (500,500),
                heightInterval = (40, 80))
shapeInfo = ShapeInfo(
                shapes = 100,
                widthInterval = (10, 20), 
                heightInterval = (10, 150))

tf.logging.set_verbosity(tf.logging.INFO)

  # Input Layer
  #input_layer = tf.reshape(features["x"], [-1, 64, 64, 1])

#conv1 = tf.layers.conv2d(
#    inputs=input_layer,
#    filters=32,
#    kernel_size=[5, 5],
#    padding="same",
#    activation=tf.nn.relu)

#print ("X = " + str(X))
#print ("Y = " + str(Y))

ShapeDict = ShapeGenerator.GenerateImageWithShapes(imageInfo, shapeInfo)

#print(ShapeDict["ShapeList"][0])

cv2.imshow('image',ShapeDict["Image"])
cv2.waitKey(0)
cv2.destroyAllWindows()