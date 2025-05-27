try:
    # Code that might raise different exceptions
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")