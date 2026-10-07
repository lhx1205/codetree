a, b = map(int, input().split())
num_val = 1
for i in range(a, b+1):
    num_val = num_val * i
print(num_val)