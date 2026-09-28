a,b = list(input().split())
c,d = list(input().split())
a = int(a)
c = int(c)
if (a >= 19 and b == "M") or (c >= 19 and d == "M"):
    print(1)

else:
    print(0)