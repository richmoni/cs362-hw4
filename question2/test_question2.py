from question2 import list_avg
import unittest


class TestListAvg(unittest.TestCase):

    def test_list_avg(self):
        '''Test list_avg() with a valid list of integers'''
        self.assertEqual(list_avg([4, 6, 8]), 6, "Should return 6")

    def test_list_avg_empty_list(self):
        '''Test list_avg() with an empty list'''
        self.assertEqual(list_avg([]), -1, "Should return -1")

    def test_list_avg_type_conflict(self):
        '''Test list_avg() with an element of invalid type in the list'''
        self.assertEqual(
            list_avg([4, 6, "This is a string"]), -1, "Should return -1")


if __name__ == '__main__':
    unittest.main()
