A, B = map(int,input().split())
for i in range(21):
    m = A//B # 몫
    n = A % B # 나머지
    A = n * 10 # 나머지에 10 곱하고 똑같이 그대로 나눔

    print(m, end="") #계속 나눈 몫인 m값을 적어나가고,
    if i==0:
        print(".",end="") # 앞에서 0이 나오면 .으로 나타냄