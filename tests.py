import unittest
import task
import math
from datetime import date


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testComputeArea(self):
        self.assertEqual(task.computeArea(3), math.pi*3*3)
        self.assertEqual(task.computeArea(0), 0)
        self.assertEqual(task.computeArea(1), math.pi*1*1)

    def testFirstLastList(self):
        self.assertEqual(task.firstLastList([1, 2, 3]), (1, 3))
        self.assertEqual(task.firstLastList([0, 1]), (0, 1))
        self.assertEqual(task.firstLastList([2, 3, 4, 9, 7]), (2, 7))

    def testComputeDays(self):
        self.assertEqual(task.computeDays(date(2009, 8, 12), date(2009, 8, 15)), 3)
        self.assertEqual(task.computeDays(date(2011, 4, 5), date(2011, 4, 4)), 1)
        self.assertEqual(task.computeDays(date(2017,5,1),date(2017,5,1)), 0)


if __name__ == '__main__':
    unittest.main()
