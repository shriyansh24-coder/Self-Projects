#To-Do List

print("Lets Prpare Your To-Do List")

def to_do():
    l1 = input("Enter the First most important thing You want to do After You Wake-Up: ")
    l2 = input("Enter the Second most important thing You want to do After You Wake-Up: ")
    l3 = input("Enter the Third most important thing You want to do After You Wake-Up: ")
    return l1, l2, l3

def show():
    print(l1)
    print(l2)
    print(l3)

# collect items and display
l1, l2, l3 = to_do()
show()