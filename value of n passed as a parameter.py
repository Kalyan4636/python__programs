def sqsum(n):
    if n == 1:
       return 1
    return n*n+sqsum(n-1)

n=int(input("enter value of n:"))
print(sqsum(n)) 