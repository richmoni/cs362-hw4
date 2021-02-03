from question3 import full_name
import unittest


class TestFullName(unittest.TestCase):

    def test_full_name_fname_and_lname(self):
        '''Test full_name() with a first and last name'''
        self.assertEqual(full_name("Isamu", "Richmond"),
                         "Isamu Richmond", "Should return \"Isamu Richmond\"")

    def test_full_name_fname_only(self):
        '''Test full_name() with only a first name'''
        self.assertEqual(full_name("Isamu", ""), "Isamu",
                         "Should return \"Isamu\"")

    def test_full_name_lname_only(self):
        '''Test full_name() with only a last name'''
        self.assertEqual(
            full_name("", "Richmond"), "Richmond", "Should return \"Richmond\"")


if __name__ == '__main__':
    unittest.main()
