def test1():
    print("this is first function with print and without calling")
#  this will not print anything

def test2():
    print("this is my 2nd function with print and calling")
# this will print because you have mentioned print in def function
test2()
print("2nd print :", type(test2()))

def test3():
    return "this is my 3nd function with return and without return"
# this will not print without print
test3()
print("3rd return: ", type(test3()))
def test4():
    return "this is my 4th function with return and print"
# this will not print without print

print(test4())
print("4th return : ", type(test4()))

# print will print the data as NonType
# return print the datatype as it is.