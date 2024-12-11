


# test_employee.py

import pytest
from employee import Employee  # Import the Employee class from 11_03_employee.py

# Test default raise of $5,000
def test_give_default_raise():
    employee = Employee('John', 'Doe', 50000)
    employee.give_raise()  # Apply default raise of $5,000
    assert employee.annual_salary == 55000  # Expected salary after raise

# Test custom raise
def test_give_custom_raise():
    employee = Employee('Jane', 'Doe', 50000)
    employee.give_raise(10000)  # Apply custom raise of $10,000
    assert employee.annual_salary == 60000  # Expected salary after custom raise
