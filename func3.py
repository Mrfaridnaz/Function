import logging

logging.basicConfig(
    filename="test1.log",
    level=logging.INFO,
    format='%(levelname)s %(asctime)s %(name)s %(message)s')

def test():
    logging.info("this is my first function")

# return
def test1():
    logging.info("this is my function with return no print")

def test2():
    logging.info("this is function with return")
