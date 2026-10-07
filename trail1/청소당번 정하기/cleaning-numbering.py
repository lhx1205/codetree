n = int(input())
a = 0
b = 0 
c = 0
for i in range(1,n+1):
    if i % 12 == 0: 
        c += 1
    elif i % 3 == 0: # 12에 포함 안 된 애들
        b += 1
    elif i % 2 == 0: # 12로도 3으로도 안 나뉘는 애들
        a += 1
print(f'{a} {b} {c}')