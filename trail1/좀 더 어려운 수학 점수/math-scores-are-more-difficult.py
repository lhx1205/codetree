a, b = list(map(int,input().split()))
c, d = list(map(int,input().split()))

if a > c:
    print("A")
elif c > a:
    print("B")
elif a == c and b > d:
    print("A")
elif a == c and d > b:
    print("B")
