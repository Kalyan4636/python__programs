def backprint(s):
    n = len(s)
    if n == 0:
        return
    print(s[-1], end = '')
    backprint(s[0:-1])
#_main_
s = input("enter a string : ")
backprint(s)