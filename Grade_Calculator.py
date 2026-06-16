sub1 = int(input("Enter Marks for 1st Subject: "))
sub2 = int(input("Enter Marks for 2nd Subject: "))
sub3 = int(input("Enter Marks for 3rd Subject: "))
sub4 = int(input("Enter Marks for 4th Subject: "))
sub5 = int(input("Enter Marks for 5th Subject: "))

total = (sub1 + sub2 + sub3 + sub4 + sub5)/5

print(f"Total Percentage obtained in all 5 Subjects is {total}%")

if total > 100:
    print("Invalid Marks Entered")
elif total >= 90:
    print("Grade A")
elif total >= 80:
    print("Grade B")
elif total >= 70:
    print("Grade C")
elif total >= 60:
    print("Grade D")
elif total >= 55:
    print("Grade E")
else:
    print("Failed in the Exam")