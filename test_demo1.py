import unittest
import requests  # only here to trigger linter rule

class DemoTestCase(unittest.TestCase):

    def setUp(self):
        self.some_list = [0, 1, 2]
        self.someOtherThing = None

    def test_list1(self):
        self.assertEqual(len(self.some_list), 3)

    def test_list2(self):
        self.assertTrue( 0 in self.some_list )
#        break  # only here to trigger linter rule

    def test_list3_fails(self):
        self.assertTrue( 9 in self.some_list )


if __name__ == '__main__':
    unittest.main()
