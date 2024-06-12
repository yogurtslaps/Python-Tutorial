def factorial(number: int) -> int:
    if type(number) != int:
        raise TypeError("Factorials apply to integers only")
    if number == 0:
        return 1
    return factorial(number-1) * number

def main():
    n = 5
    print(factorial(5.2))

if __name__ == "__main__":
    main()