from ShapeGenerator import ShapeGenerator, ImageInfo, ShapeInfo

import numpy as np
import cv2


ShapeDict = ShapeGenerator.GenerateImageWithShapes(
    ImageInfo(
        size = (600,600),
        heightInterval = (40, 80)),
    ShapeInfo(
        shapes = 50,
        widthInterval = (10, 50), 
        heightInterval = (10, 150)))

cv2.imshow('image',ShapeDict["Image"])
cv2.waitKey(0)
cv2.destroyAllWindows()