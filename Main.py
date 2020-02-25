import re
import evaluteEXpr
import EvaluateSqrt
import EvaluatePowe
import storehistory
import config_logger

class main1():
    def calc(self):
        finish = 1
        typeof= "cat1"
        while (finish):
            select_operation = input(
                "Select Operation to calculate 1:Arithmetic_Operations  2:SquareRoot  3.PowerOf 4.See_History 5.finish:: ")
            if select_operation == '1':
                try:
                    user_input = input("Enter expression or numbers to calculate Arithmetic_Operations:")
                    regex = re.compile('[@_!#$%^&()<>?\|=}{~:]')
                    if (regex.search(user_input) != None):
                        print("invalid Expression")
                        logger=config_logger.readconfig()
                        logger.error("Expression not valid")
                    else:
                        lst = re.findall(r'[0-9\.]+|[^0-9\.]+', user_input)
                        result = evaluteEXpr.calculateArithmeticOperations(lst)
                        storehistory.store_as_history(user_input, result)
                        storehistory.connect(result, typeof)

                except (ArithmeticError, ValueError, EOFError):

                    logger = config_logger.readconfig()
                    logger.error("Value Error")
                    print("ArithmeticError")

            if select_operation == '2':
                user_input = int(input("Enter number to calculate SquareRoot:"))
                result = EvaluateSqrt.calculateSquareRoot(user_input)
                storehistory.store_as_history(user_input, result)
                storehistory.connect(result, typeof)

            if select_operation == '3':
                s = input("enter number and power(mind whitespace between them)").split()
                if len(s) != 2:
                    print("Enter 2 numbers to calculate Power")

                    logger = config_logger.readconfig()
                    logger.error("Value error")
                    break
                else:
                    a = int(s[0])
                    b = int(s[1])

                result = EvaluatePowe.calculatePowerof(a, b)
                storehistory.store_as_history(' '.join(s), result)
                storehistory.connect(result, typeof)

            if select_operation == '4':
                his = storehistory.getdata(typeof)
                print(his)

                logger = config_logger.readconfig()
                logger.info("History is displayed")
            if select_operation == '5':
                    finish = 0
