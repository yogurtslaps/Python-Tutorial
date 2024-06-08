#Write a program to print the Fibonacci sequence for a count given by the user. 
num=int(input("Enter the range number:"))
a=0
b=1
for n in range(0,num):
    if n<=1:
        next = n
    else:
        next=a+b
        a=b
        b=next
    print(next)


