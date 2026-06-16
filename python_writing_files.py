#Python program to write data to a text file

employees = ["Alice", "Bob", "Charlie", "David"]

#txt_data = "I am SpooderMan."

file_path = "text.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print("Data has been written to the file.")
except FileExistsError:
    print("The file already exists.")