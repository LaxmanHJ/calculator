
import modules.evaluteEXpr as evaluteEXpr
import modules.EvaluatePowe as EvaluatePowe
import modules.EvaluateSqrt as EvaluateSqrt
import unittest

class TestCalculator(unittest.TestCase):
    @classmethod
    def setupclass(self):
        print("setup class")

    def testArithmetic_oper(self):
        self.assertEqual(evaluteEXpr.calculateArithmeticOperations('2+3-3'),2)
        self.assertEqual(evaluteEXpr.calculateArithmeticOperations('2*3-3'),3)

class Testevaluate_sqrt(unittest.TestCase):
    def testSqry(self):
        self.assertEqual(EvaluateSqrt.calculateSquareRoot(4),2)
        self.assertEqual(EvaluateSqrt.calculateSquareRoot(16),4)

class Testevaluate_pow(unittest.TestCase):
    def testpow(self):
        self.assertEqual(EvaluatePowe.calculatePowerof(2,2),4)

if __name__=='__main__':            #testloader
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCalculator)

    unittest.TextTestRunner().run(suite)