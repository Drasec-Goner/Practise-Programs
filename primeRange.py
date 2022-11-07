#Write a program to display all prime numbers within a range
#Take the user input for start and end of range.

start = int(input("Enter the Starting Range: "))
end = int(input("Enter the Ending Range: "))

for i in range(start,end):
    flag = 1
    for j in range(2, i):
        if i%j==0:
            flag=0
            break
    if flag ==1 and i>1:
        print(i)
        flag = 0