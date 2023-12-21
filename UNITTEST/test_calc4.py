import unittest
import calc
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(1,5),6)
        self.assertEqual(calc.add(-4,-1),-6)
    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(1,5),-4)
        self.assertEqual(calc.sub(-4,-1),-3)
    def test_mul(self):
        self.assertEqual(calc.mul(10,5),50)
        self.assertEqual(calc.mul(1,5),5)
        self.assertEqual(calc.mul(-4,-1),4)
    def test_div(self):
        self.assertEqual(calc.div(10,5),2.2)
        self.assertEqual(calc.div(1,5),0.2)
        self.assertEqual(calc.div(-4,-1),4)
if __name__=='__main__':
    unittest.main()

'''
FF..
======================================================================
FAIL: test_add (__main__.TestCalc.test_add)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\jayak\Downloads\Python-Documentation\UNITTEST\test_calc4.py", line 7, in test_add
    self.assertEqual(calc.add(-4,-1),-6)
AssertionError: -5 != -6

======================================================================
FAIL: test_div (__main__.TestCalc.test_div)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\jayak\Downloads\Python-Documentation\UNITTEST\test_calc4.py", line 17, in test_div
    self.assertEqual(calc.div(10,5),2.2)
AssertionError: 2.0 != 2.2

----------------------------------------------------------------------
Ran 4 tests in 0.003s

FAILED (failures=2)
'''