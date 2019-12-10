def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            str = "FizzBuzz"
            print(str, end="")
        elif x % 3 == 0:
            str = "Fizz"
            print(str, end="")
        elif x % 5 == 0:
            str = "Buzz"
            print(str, end="")
        else:
            print(x, end="")
        print(" ", end="")
