# write a function to extract the list from the list
l = [4,5,6,67,7,8,8,9,9,9, [3,4,5,6,7,7] , "sudh"]

def lis1(a):
    for i in l:
        if type(i) == list:
            return i
print(lis1(l))

# =========================================================
l = [4,5,6,67,7,8,8,9,9,9, [3,4,5,6,7,7],[2,3,4] , "sudh"]
def lis1(a):
    li = []
    for i in l:
        if type(i) == list:
            li.append(i)
    return li
print(lis1(l))

# =========================================================
l = [4,5,6,67,7,8,8,9,9,9, [3,4,5,6,7,7],[2,3,4] , "sudh"]
def lis1(a):
    li = []
    for i in l:
        if type(i) == list or type(i) == str:
            li.append(i)
    return li
print(lis1(l))