


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee's first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add a raise to the employee's salary (default $5,000)."""
        self.annual_salary += amount
