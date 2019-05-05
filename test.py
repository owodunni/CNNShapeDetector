import unittest
from ShapeGenerator import *

class TestShape(unittest.TestCase):
    def test_shapeOverlap(self):
        shape1 = Shape(ShapeType.circle, 0, 1, (0,0))
        shape2 = Shape(ShapeType.circle, 0, 1, (0,0))

        self.assertTrue(shape1.Overlap(shape2))
    

    def test_shapeNoOverlapX(self):
        shape1 = Shape(ShapeType.circle, 0, 1, (0,0))
        shape2 = Shape(ShapeType.circle, 0, 1, (5,0))

        self.assertFalse(shape1.Overlap(shape2))

class TestShapeGenerator(unittest.TestCase):
    def test_generateSamples(self):
        imageInfo = ImageInfo(
                size = (64,64),
                heightInterval = (40, 80))
        shapeInfo = ShapeInfo(
                shapes = 1,
                widthInterval = (20, 50),
                heightInterval = (10, 150))
        
        samples, labels = ShapeGenerator.GenerateSamples(imageInfo, shapeInfo, 2)


        self.assertEqual(samples.shape, (2, 64, 64))
        self.assertEqual(labels.shape, (2,))

    def test_generateDataSet(self):
        imageInfo = ImageInfo(
                size = (64,64),
                heightInterval = (40, 80))
        shapeInfo = ShapeInfo(
                shapes = 1,
                widthInterval = (20, 50),
                heightInterval = (10, 150))

        (train_images, train_labels),(test_images, test_labels) = ShapeGenerator.GenerateDataSet(
            imageInfo, shapeInfo, 4, 2)
        
        self.assertEqual(train_images.shape, (4, 64, 64))
        self.assertEqual(train_labels.shape, (4,))
        self.assertEqual(test_images.shape, (2, 64, 64))
        self.assertEqual(test_labels.shape, (2,))