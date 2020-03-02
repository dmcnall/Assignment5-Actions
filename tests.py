import unittest
import task

class TestCase(unittest.TestCase):


    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testComputeArea(self):
        self.assertEqual(task.computeArea(3), 3.14*3*3)
        self.assertEqual(task.computeArea(0), 0)
        self.assertEqual(task.computeArea(1), 3.14*1*1)


if __name__ == '__main__':
    unittest.main()
