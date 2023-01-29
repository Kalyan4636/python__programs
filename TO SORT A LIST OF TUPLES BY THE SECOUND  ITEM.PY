def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup
tup =[('for' , 2), ('is' , 9), ('to' , 7), ('go' , 5), ('or' , 15), ('a' , 13)]
print(Sort_Tuple(tup))