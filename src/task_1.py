
# Task 1: Python Core, OOP and Errors

def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"{self.name} earns {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, "
            f"Salary: {self.salary}, "
            f"Team size: {self.team_size}"
        )


employees = [
    {"id": 1, "name": "Arun", "department": "Sales",
     "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR",
     "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT",
     "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT",
     "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance",
     "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales",
     "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT",
     "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR",
     "salary": 48000, "city": "Mumbai"}
]

# List comprehension
above_50000 = [
    e["name"] for e in employees if e["salary"] > 50000
]
print("Above 50000:", above_50000)

# map and lambda: add a 10% raise
raised_salaries = list(
    map(lambda e: e["salary"] * 1.10, employees)
)
print("Raised salaries:", raised_salaries)

# filter: keep Chennai employees
chennai = list(
    filter(lambda e: e["city"] == "Chennai", employees)
)
print("Chennai:", [e["name"] for e in chennai])

# Function with *args and **kwargs
print("Bonus:", bonus(50000, 0.1, 500, 1000, cap=6000))

# OOP and inheritance
employee = Employee("Arun", 30000)
print("Annual salary:", employee.annual_salary())

manager = Manager("Priya", 80000, 5)
print(manager.get_details())

# Exception handling
try:
    Employee("Test", -500)
except InvalidSalaryError as error:
    print("Error:", error)
finally:
    print("Transaction finished")

# continue and break
for salary in [0, 30000, 90000, 60000]:
    if salary == 0:
        continue

    if salary > 85000:
        print("Stopping at:", salary)
        break

    print("Salary:", salary)
