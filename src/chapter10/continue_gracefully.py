while True:
    try:
        # Code that might raise different exceptions
        number = int(input("Enter a positive number: "))
        result = 10 / number
    except ValueError:
        print("That's not a valid integer. Please try again.")
    except ZeroDivisionError:
        print("That's not a positive number. Please try again.")