def SortTuple(tup):
    n = len(tup)

    for i in range(n):
        for j in range(n-i-1):

            if tup[j][0] > tup[j + 1][0]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]
    return tup

tup = [("Aditya", 20), ("kalyan", 32), ("Ashwani", 22), ("Shubham", 32), ("Penny", 52), ("Rita", 62)]
print(SortTuple(tup))
