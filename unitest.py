
import evaluteEXpr
import EvaluatePowe
import EvaluateSqrt
import unittest

class TestCalculator(unittest.TestCase):
    @classmethod
    def setupclass(self):
        print("setup class")

    def testArithmetic_oper(self):
        self.assertEqual(evaluteEXpr.calculateArithmeticOperations('2+3-3'),2)
        self.assertEqual(evaluteEXpr.calculateArithmeticOperations('2*3-3'),3)
        with self.assertRaises(TypeError):
            print("Typeeror")


    def testSqry(self):
        self.assertEqual(EvaluateSqrt.calculateSquareRoot(4),2)
        self.assertEqual(EvaluateSqrt.calculateSquareRoot(16),4)

    def testpow(self):
        self.assertEqual(EvaluatePowe.calculatePowerof(2,2),4)
if __name__ == '__main__':
    unittest.main()