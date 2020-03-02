import unittest
import task
import math 

class TestCase(unittest):

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

if __name__ == '__main__':
    unittest.main()
