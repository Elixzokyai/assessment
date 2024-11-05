# Base class
class Employee:
    def calculate_salary(self):
        print("Calculating salary for an employee.")

# Subclass
class Manager(Employee):
    def calculate_salary(self):
        # Specific calculation logic for a manager's salary
        base_salary = 50000
        bonus = 10000
        total_salary = base_salary + bonus
        print(f"Manager's total salary is: ${total_salary}")

# Demonstrate overridden behavior
employee = Employee()
manager = Manager()

print("Employee's Salary Calculation:")
employee.calculate_salary()  # Calls the method in Employee class

print("\nManager's Salary Calculation:")
manager.calculate_salary()    # Calls the overridden method in Manager class
