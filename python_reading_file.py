#Python FIle Reading

file_path = "text.txt"

try:  
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")