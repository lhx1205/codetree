a , b = map(int,input().split())
num_val = 1
for i in range(1, b+1):
    if i % a == 0:
        num_val *= i
print(num_val)