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

<<<<<<< HEAD
def test2():
    logging.info("this is function with return")
=======
# return
def test1():
    return "this is my first function"

test1()

def test2():
    return "this is my first function with return"

print(test2())
>>>>>>> origin/main
