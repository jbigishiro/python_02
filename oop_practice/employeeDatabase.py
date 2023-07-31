# Exercise: Employee Database Management

# Create a class called Employee.

# The class should have the following attributes:

# employee_id (a unique identifier for each employee).
# name (the name of the employee).
# position (the job position of the employee).
# salary (the salary of the employee).
# The class should have the following methods:

# display_employee_info(): Displays information about the employee (employee_id, name, position, and salary).
# Create a class called EmployeeDatabase.

# The class should have the following attribute:

# employees (a list to store all the Employee instances in the database).
# The class should have the following methods:

# add_employee(employee): Adds an Employee instance to the database.
# remove_employee(employee_id): Removes an employee from the database based on their employee_id.
# find_employee_by_id(employee_id): Returns the Employee instance with the given employee_id, if it exists in the database.
# find_employee_by_name(name): Returns a list of Employee instances with the given name, if any.
# display_all_employees(): Displays information about all the employees in the database.
# Test your classes by creating instances of Employee and EmployeeDatabase. Add some employees to the database, perform operations like adding/removing employees, searching for employees, and displaying employee information.

# Example Usage:

# python
# Copy code
# # Create employee instances
# employee1 = Employee(101, 'John Doe', 'Software Engineer', 60000)
# employee2 = Employee(102, 'Jane Smith', 'Data Analyst', 55000)
# employee3 = Employee(103, 'Michael Johnson', 'Product Manager', 70000)

# # Create employee database instance
# employee_database = EmployeeDatabase()

# # Add employees to the database
# employee_database.add_employee(employee1)
# employee_database.add_employee(employee2)
# employee_database.add_employee(employee3)

# # Display information about all employees in the database
# employee_database.display_all_employees()

# # Find employee by employee_id
# found_employee = employee_database.find_employee_by_id(102)
# if found_employee:
#     found_employee.display_employee_info()
# else:
#     print("Employee not found.")

# # Find employees by name
# found_employees = employee_database.find_employee_by_name('John Doe')
# if found_employees:
#     for employee in found_employees:
#         employee.display_employee_info()
# else:
#     print("No employees found with the given name.")

# # Remove employee from the database
# employee_database.remove_employee(101)

# # Display updated information about all employees in the database
# employee_database.display_all_employees()
# Expected Output:

# yaml
# Copy code
# Employee ID: 101, Name: John Doe, Position: Software Engineer, Salary: $60000
# Employee ID: 102, Name: Jane Smith, Position: Data Analyst, Salary: $55000
# Employee ID: 103, Name: Michael Johnson, Position: Product Manager, Salary: $70000
# Employee ID: 102, Name: Jane Smith, Position: Data Analyst, Salary: $55000
# Employee ID: 101, Name: John Doe, Position: Software Engineer, Salary: $60000
# Employee ID: 102, Name: Jane Smith, Position: Data Analyst, Salary: $55000
# Employee ID: 103, Name: Michael Johnson, Position: Product Manager, Salary: $70000
# In this exercise, we created two classes: Employee and EmployeeDatabase. The Employee class represents individual employees with attributes (employee_id, name, position, and salary). The EmployeeDatabase class serves as the employee database management system and contains methods for adding/removing employees, finding employees by ID or name, and displaying information about all employees in the database.

# The example usage demonstrates how to create instances of Employee and EmployeeDatabase, add employees to the database, perform operations like adding/removing employees, searching for employees, and displaying employee information.


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")


class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [employee for employee in self.employees if employee.employee_id != employee_id]

    def find_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def find_employee_by_name(self, name):
        found_employees = []
        for employee in self.employees:
            if name.lower() in employee.name.lower():
                found_employees.append(employee)
        return found_employees

    def display_all_employees(self):
        print("All Employees in the Database:")
        for employee in self.employees:
            employee.display_employee_info()


# Example Usage
employee1 = Employee(101, 'John Doe', 'Software Engineer', 60000)
employee2 = Employee(102, 'Jane Smith', 'Data Analyst', 55000)
employee3 = Employee(103, 'Michael Johnson', 'Product Manager', 70000)

employee_database = EmployeeDatabase()

employee_database.add_employee(employee1)
employee_database.add_employee(employee2)
employee_database.add_employee(employee3)

employee_database.display_all_employees()

found_employee = employee_database.find_employee_by_id(102)
if found_employee:
    found_employee.display_employee_info()
else:
    print("Employee not found.")

found_employees = employee_database.find_employee_by_name('John Doe')
if found_employees:
    for employee in found_employees:
        employee.display_employee_info()
else:
    print("No employees found with the given name.")

employee_database.remove_employee(101)

employee_database.display_all_employees()
