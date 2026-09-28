# 1 3 5 7 8 10 12 = 31
# 2 = 28
# 4 6 9 11 = 30

n = int(input())
if n == 1 or n == 3 or n == 5 or n== 7 or n==8 or n== 10 or n== 12:
    print(31)
elif n == 2:
    print(28)
else:
    print(30)