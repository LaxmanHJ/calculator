import re
import evaluteEXpr
import EvaluateSqrt
import EvaluatePowe
import storehistory
import logging:

def main():
    logging.basicConfig(filename="newfile.log",
                        format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                        filemode='w')

    # Creating an object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    finish = 1
    while (finish):
        # select_operation = input(
        #     "Select Operation to calculate 1:Arithmetic_Operations  2:SquareRoot  3.PowerOf 4.See_History 5.finish:: ")
        select_operation=getoption()
        if select_operation == '1':
            try:
                user_input = input("Enter expression or numbers to calculate Arithmetic_Operations:")
                lst = re.findall(r'[0-9\.]+|[^0-9\.]+', user_input)
                result = evaluteEXpr.calculateArithmeticOperations(lst)
                storhistory.store_as_history(user_input,result)
                storhistory.connect(result)

            except (ArithmeticError,ValueError,EOFError):
                print("ArithmeticError")

        if select_operation == '2':
            user_input = int(input("Enter number to calculate SquareRoot:"))
            result =EvaluateSqrt.calculateSquareRoot(user_input)
            hist=storehistory.store_as_history(user_input,result)
            storehistory.connect(result)

        if select_operation == '3':
            s = input("enter number and power(mind whitespace between them)").split()
            if len(s)!=2:
                print("Enter 2 numbers to calculate Power")
                logger.warning("Its a Warning")

                break
            else:
                a = int(s[0])
                b = int(s[1])



            result = EvaluatePowe.calculatePowerof(a, b)
            hist=storehistory.store_as_history(' '.join(s),result)
            storehistory.connect(result)

        if select_operation == '4':
            his=storehistory.getdata()
            print(his)

        if select_operation == '5':
            finish = 0

        logger.debug("Harmless debug Message")



def getoption():
    id=input("Enter Customer Category")
    if id=='1':
        select_operation = input(
            "Select Operation to calculate 1:Arithmetic_Operations  2:SquareRoot  3.PowerOf 4.See_History 5.finish:: ")
        return select_operation
    elif id=='2':
        select_operation = input(
            "Select Operation to calculate 1:Arithmetic_Operations   4.See_History 5.finish:: ")
        return select_operation
    elif id == '3':
        select_operation = input(
            "Select Operation to calculate  2:SquareRoot  3.PowerOf  4.See_History 5.finish:: ")
        return select_operation


if __name__ == '__main__':

    main()

