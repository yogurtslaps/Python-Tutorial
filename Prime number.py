#Write a program to print all the prime numbers between 2 and a number (N) given by the user. 

x=2
y=int(input("Enter your number:"))

print("The prime numbers between",x,"and",y,"are")
for num in range(x,y):
    if num>1:
            for i in range(2,num):
                if(num%i)==0:
                     break
                else:
                     print(num)