# find the index number of 7 and 6
t = (3,4,5,6,67,7,87,)
a=-1
while a>=-len(t):
    if t[a]==6 or t[a]==7 :
        print('index of ',t[a], ' is ',a)
    a=a-1

def test8(t):
    a=-1
    while a>=-len(t):
        if t[a]==6 or t[a]==7 :
            print('index of ',t[a], ' is ',a)
        a=a-1
test8((3,4,4,6,6,7,7,7,88))