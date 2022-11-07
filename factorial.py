# Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.

n = int(input("Enter a Number: "))
f=1
for i in range(1,n+1):
    f = f*i
print("Factorial:",f)