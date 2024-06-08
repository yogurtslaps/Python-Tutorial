#Write a program that calculates the factorial of a number given by the user, then prints the output. 
n=int(input("Enter your number:"))
factorial=1
if n==0:
    print(1)
else:
    for i in range(1,n+1):
        factorial = factorial*i
print("The factorial of",n,"is",factorial)

