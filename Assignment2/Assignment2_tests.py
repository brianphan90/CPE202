from infix import *
from radix import *
import unittest

DIGITS = 3

class Asg2(unittest.TestCase):
    def test_infix_1(self):
        e = '( 1 + 2 ) * 2 * ( 2 + 1 )'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 18.0, places = DIGITS)
        
    def test_infix_2(self):
        e = '( 1 )'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 1, places = DIGITS)
        
    def test_infix_3(self):
        e = '( ( 1 + 2 ) * 2 ) / ( 2 + 1 )'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 2, places = DIGITS)
        
    def test_infix_4(self):
        e = '( 20 + 2 ) * 2 * 2 + 1 '
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 89, places = DIGITS)
        
    def test_infix_5(self):
        e = '1 + 1 + 1 + 1'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 4, places = DIGITS)
        
    def test_infix_6(self):
        e = '20 / 20'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 1, places = DIGITS)
        
    def test_infix_7(self):
        e = '50 / -2'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, -25.0, places = DIGITS)
        
    def test_infix_8(self):
        e = '( ( ( ( ( 10 ) ) ) ) )'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 10, places = DIGITS)
        
    def test_infix_9(self):
        e = '( ( 10 + 10 ) * ( 2 / 2 ) )'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 20, places = DIGITS)
        
    def test_infix_10(self):
        e = '( ( -10 + 10 ) * ( 2 / 2 ) )'
        val = eval_infix(e)        
        self.assertAlmostEqual(val, 0, places = DIGITS)   
if __name__ == '__main__':  
    unittest.main()
