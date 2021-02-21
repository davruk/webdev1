print("Welcome to the FizzBuzz game!")
end = int(input("Please, enter the number between 1 and 100: "))

for num in range(1, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 == 0:
        print("fizz")
        continue
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

