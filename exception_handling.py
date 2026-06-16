#Exception handling

try:
 number = int(input("Enter a number: "))
 print(1/number)
except ZeroDivisionError:
 print("You cannot divide by zero!")
except ValueError:
 print("Please enter a valid number!")
finally:
 print("This will always be executed.") 