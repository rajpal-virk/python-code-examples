# importing libraries
import unittest
import sys
sys.path.append('/Users/rajpalvirk/GitHub/python-code-examples/src')
from sum2num import sum2num

class TestSumValues(unittest.TestCase):
    def test_sum(self):
        self.assertAlmostEqual(sum2num(2,3), 5)
        self.assertAlmostEqual(sum2num(2.5,3), 5.5)
        self.assertAlmostEqual(sum2num(2.5,3.25), 5.75)
    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, sum2num, ('2',3))
        self.assertRaises(TypeError, sum2num, (2,'3'))
        self.assertRaises(TypeError, sum2num, (2,True))
        self.assertRaises(TypeError, sum2num, (True,3))