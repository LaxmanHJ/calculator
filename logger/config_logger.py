import configparser
import logging

def readconfig():
    config= configparser.ConfigParser()
    config.read('config_Debugger.ini')
    logging.basicConfig(filename=config['debug']['filename'],
                        format=config['debug']['format'],
                        filemode=config['debug']['filemode'])

    # Creating an object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    return logger


