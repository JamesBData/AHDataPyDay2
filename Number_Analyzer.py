# Data Analyzer Project Day 2
name = input("What is your name? ")
number = (int(input("Enter a number between 1 and 100 inclusive: ")))

if (number % 2) == 0 and number in range(2,24+1):
    print(name + ", your number is even and less than 25")

if (number % 2) == 0 and number in range(26,60+1):
    print(name + ", your number is even and inclusive between 26 and 60. ")

if (number % 2) == 1 and number < 60:
    print(name + ", your number is odd and less than 60.")

if number > 60 and (number % 2) == 0:
    print(str(number) + " is even and greater than 60, " + name + ".")

if number > 60 and (number % 2) == 1:
    print(str(number) + " is odd and greater than 60, " + name + ".")









