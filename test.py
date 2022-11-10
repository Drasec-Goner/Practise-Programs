a = int(input())
b = int(input())

for i in range(a,b+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if i==s:
        print(i,end=" ")
        if i%2!=0:
            break