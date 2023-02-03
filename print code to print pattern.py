n = 5
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(i, n):
        if(i%2==0):
            print("z", end=' ')
        else:
             print("0", end=' ')
    print()