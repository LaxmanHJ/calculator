import re
import evaluteEXpr
import config_logger
import storehistory


class main2():
    def calc(self):
        finish = 1
        typeof = "cat2"
        while (finish):
            select_operation = input(
                "Select Operation to calculate 1:Arithmetic_Operations  2.See_History 3.finish:: ")
            if select_operation == '1':
                try:
                    user_input = input("Enter expression or numbers to calculate Arithmetic_Operations:")
                    regex = re.compile('[@_!#$%^&()<>?\|=}{~:]')
                    if (regex.search(user_input) != None):
                        print("Expression is not is accepted")

                        logger = config_logger.readconfig()
                        logger.error("Expression not valid")
                    else:
                        lst = re.findall(r'[0-9\.]+|[^0-9\.]+', user_input)
                        result = evaluteEXpr.calculateArithmeticOperations(lst)
                        storehistory.store_as_history(user_input, result)
                        storehistory.connect(result,typeof)

                except (ArithmeticError, ValueError, EOFError):
                    print("ArithmeticError")
                    logger = config_logger.readconfig()

                    logger.error("ArithmeticError ")

            if select_operation == '2':
                his = storehistory.getdata(typeof)
                print(his)
                logger = config_logger.readconfig()

                logger.info("Histroy is displayed")

            if select_operation == '3':
                finish = 0


