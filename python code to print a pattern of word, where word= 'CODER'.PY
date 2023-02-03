s = "CODER"
n = len(s)
p = 0
for i in range(n):
    for j in range(i+1):
        print(s[p], end = ' ')
    p+=1
    print()