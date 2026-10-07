N = int(input())
y = 0 # 윤년
for i in range(1,N+1):
    if i % 4 ==0:
        y += 1
        if i % 100 == 0 and i % 400 != 0:
            y -= 1
print(y)

