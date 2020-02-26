import math
import logger.config_logger as config_logger
def calculateSquareRoot(num):

    try:
        result = math.sqrt(num)
        print(float(result))
        return result
    except:
        logger = config_logger.readconfig()

        logger.error("Negative Entry")

        print("Negative numbers donot have sqrt")