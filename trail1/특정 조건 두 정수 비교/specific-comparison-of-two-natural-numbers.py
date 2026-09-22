A, B = list(map(int, input().split()))
if A < B:
    print(1, end=" ")
elif A >= B:
    print(0, end=" ")
if A == B:
    print(1, end=" ")
elif A != B:
    print(0, end=" ")