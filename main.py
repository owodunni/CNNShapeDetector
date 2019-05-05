#!/usr/bin/env python3
from ShapeGenerator import ShapeGenerator, ImageInfo, ShapeInfo

import numpy as np
import cv2
import tensorflow as tf

imageInfo = ImageInfo(
                size = (64,64),
                heightInterval = (0, 100))
shapeInfo = ShapeInfo(
                shapes = 1,
                widthInterval = (20, 50),
                heightInterval = (10, 150))

tf.logging.set_verbosity(tf.logging.INFO)

nmbTrainSamples = 1000
nmbTestSamples = 100

(train_images, train_labels), (test_images, test_labels) = ShapeGenerator.GenerateDataSet(
    imageInfo, shapeInfo, nmbTrainSamples, nmbTestSamples)

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

for x in range(0, nmbTrainSamples):
    cv2.imshow('image',train_images[x,:,:])
    cv2.waitKey(100)

cv2.destroyAllWindows()