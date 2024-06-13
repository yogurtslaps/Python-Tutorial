#Write the Fibonacci function you wrote in the last submodule, but this time with recursion. 

def fibonacci(n, num1, num2):
    if n < 3:
        return
    fn = num1 + num2
    num2 = num1
    num1 = fn
    print(fn, end=" ")
    fibonacci(n - 1, num1, num2)

def print_fibonacci(n):
    
    if n < 1:
        print("Invalid")
    elif n == 1:
        print(0)
    elif n == 2:
        print("0 1")
    else:
        print("0 1", end=" ")
        fibonacci(n, 1, 0)



if __name__ == "__main__":
    n = 9
    
    print_fibonacci(n)