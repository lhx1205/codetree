N = int(input())
for i in range(N,101):
    if i >= 90:
        i = "A"
    elif i >= 80:
        i = "B"
    elif i >= 70:
        i = "C"
    elif i >= 60:
        i = "D"
    else:
        i = "F"
    print(i,end=" ")
    