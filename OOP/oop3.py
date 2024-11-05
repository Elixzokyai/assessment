class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self):
        self.employees = []  # List to hold Employee objects

    def add_employee(self, name, salary):
        employee = Employee(name, salary)
        self.employees.append(employee)  # Add the employee to the list

    def calculate_total_payroll(self):
        return sum(employee.salary for employee in self.employees)  # Sum salaries of all employees

# Usage
payroll = Payroll()
payroll.add_employee("Pablo", 1000)
payroll.add_employee("Grace", 1300)
payroll.add_employee("Bob", 40000)

total_payroll = payroll.calculate_total_payroll()
print(f"Total Payroll: {total_payroll}")

# Printing employees for verification
for emp in payroll.employees:
    print(f"Employee: {emp.name}, Salary: {emp.salary}")
