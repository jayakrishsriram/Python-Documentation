import unittest
import calc
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(1,5),6)
        self.assertEqual(calc.add(-4,-1),-5)
    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(1,5),-4)
        self.assertEqual(calc.sub(-4,-1),-3)
    def test_mul(self):
        self.assertEqual(calc.mul(10,5),5)
        self.assertEqual(calc.mul(1,5),5)
        self.assertEqual(calc.mul(-4,-1),4)
    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
        self.assertEqual(calc.div(1,5),0.2)
        self.assertEqual(calc.div(-4,-1),4)
if __name__=='__main__':
    unittest.main()

'''
..F.
======================================================================       
FAIL: test_mul (__main__.TestCalc.test_mul)
----------------------------------------------------------------------       
Traceback (most recent call last):
  File "C:\Users\jayak\Downloads\Python-Documentation\UNITTEST\test_calc3.py", line 13, in test_mul
    self.assertEqual(calc.mul(10,5),5)
AssertionError: 50 != 5

----------------------------------------------------------------------       
Ran 4 tests in 0.003s

FAILED (failures=1)

'''