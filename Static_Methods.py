class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Tester"]
        return position in valid_positions
    
employee1 = Employee("Alice", "Developer")
employee2 = Employee("Bob", "Designer")
employee3 = Employee("Charlie", "Manager")

print(Employee.is_valid_position("Developer"))  # True
print(Employee.is_valid_position("Intern"))     # False

print(employee1.get_info())  # Alice is a Developer
print(employee2.get_info())  # Bob is a Designer
print(employee3.get_info())  # Charlie is a Manager