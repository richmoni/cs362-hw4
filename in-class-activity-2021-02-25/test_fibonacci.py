from fibonacci import fib
import unittest


class TestFibonacci(unittest.TestCase):
    def test_first_num_in_sequence(self):
        '''Test that the first number in the sequence is zero.'''
        self.assertEqual(fib(1), 0)

    def test_second_num_in_sequence(self):
        '''Test that the second number in the sequence is one.'''
        self.assertEqual(fib(2), 1)

    def test_third_num_in_sequence(self):
        '''Test that the third number in the sequence is one.'''
        self.assertEqual(fib(3), 1)

    def test_fourth_num_in_sequence(self):
        '''Test that the fourth number in the sequence is two.'''
        self.assertEqual(fib(4), 2)

    def test_tenth_num_in_sequence(self):
        '''Test that the tenth number in the sequence is 34.'''
        self.assertEqual(fib(10), 34)


if __name__ == '__main__':
    unittest.main()
