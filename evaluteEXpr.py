import config_logger
def calculateArithmeticOperations(expr):

    try:
            result = eval(' '.join(str(x) for x in expr))
            print(result)
            return result

    except (ZeroDivisionError,EOFError,ValueError,ArithmeticError):
        print("ZeroDivisionError")
        logger = config_logger.readconfig()

        logger.error("ZeroDivisionError ")
