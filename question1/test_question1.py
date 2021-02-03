from question1 import volume
import unittest


class TestVolume(unittest.TestCase):

    def test_volume(self):
        '''Test volume() with a valid side length'''
        self.assertEqual(volume(2), 8, "Should return 8")

    def test_volume_negative(self):
        '''Test volume() with a negative input'''
        self.assertEqual(volume(-2), -1, "Should return -1")

    def test_volume_type_conflict(self):
        '''Test volume() with an invalid type for input'''
        self.assertEqual(volume("This is a string"), -1, "Should return -1")


if __name__ == '__main__':
    unittest.main()
