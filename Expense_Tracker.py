#Expence Tracker

a = int(input("Enter Your Total Salary: "))

print(f"Your Total Salary is {a}")

e = int(input("Expense for Electricity Bill: "))

m = int(input("Expense for Milk: "))

gr = int(input("Expense for Groceries: "))

f = int(input("Expense for fuel: "))

g = int(input("Expense for gas bill: "))

v = int(input("Expense for vegetables: "))

ma = int(input("Expense for maid: "))

o = int(input("Expense for other food: "))

r = int(input("Expense for recharge: "))

print(f"Your expence are: {e + m + gr + f + g + v + ma + o + r}")

print(f"Your Bank Balance should be: {a - e - m - gr - f - g -v - ma - o - r}")