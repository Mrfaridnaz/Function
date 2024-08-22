a= 1
while a<4:
    print(a)
    a = a+1
else:
    print("print all with print state")


# The code you provided is almost correct for adding numbers to a list in a loop,
# but there is a small issue with using return outside of a function. In Python,
# return can only be used inside a function. If you want to see the result after the loop,
# you can simply print the list or if it's in a function, return it from the function.

#a = 1
#while a < 4:
    #li.append(a)
   # a = a + 1
# return li

def lis():
    a = 1
    b = 5
    li = []
    while a<b:
        li.append(a)
        a =a + 1
    return li

print(lis())


def lis(a,b):
    li = []
    while a<b:
        li.append(a)
        a =a + 1
    return li

print(lis(2,5))


