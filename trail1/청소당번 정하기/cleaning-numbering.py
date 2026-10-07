n=int(input())

#2배수 3배수 12배수 
a=0
b=0
c=0
for i in range(1,n+1):
    if i%2==0:
       a+=1
       if i%6==0:
        a-=1
    if i%3==0:
        b+=1
        if i%12==0:
            b-=1
    if i%12==0:
        c+=1
        
print(f'{a} {b} {c}')
