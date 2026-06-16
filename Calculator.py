#Calculator

print("Enter Two Numbers: ")
a = int(input())
b = int(input())

print("Choose an operator (+ , - , / , * , % ) for operation: ")
op = input().strip()

if op == '+':
	print(a + b)
elif op == '-':
	print(a - b)
elif op == '*':
	print(a * b)
elif op == '/':
	if b == 0:
		print("Error: Division by zero")
	else:
		print(a / b)
elif op == '%':
	print(a % b)
else:
	print("Unknown operator")