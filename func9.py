l = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' : "sudh", "k2" : "ineuron", "k3" : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]
for i in l :
    if type(i) == set or type(i) == list or type(i) == str or  type(i) == tuple :
        for j in i :
            if type(j) == int :
                print(j)
    if type(i) == dict :
        for j in i.items() :
            for k in j :
                if type(k) == int :
                    print(k)
