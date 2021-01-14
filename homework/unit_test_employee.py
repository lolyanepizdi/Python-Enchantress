import unittest
from tests_simple_employee import Employee
from unittest.mock import patch


class MyTestEmployee(unittest.TestCase):
    def test_email(self):
        employee = Employee('liana', 'xernez', 8000)
        self.assertEqual(employee.email, 'liana.xernez@email.com')

    def test_fullname(self):
        employee = Employee('liana', 'xernez', 8000)
        self.assertEqual(employee.fullname, 'liana xernez')

    def test_apply_raise(self):
        employee = Employee('liana', 'xernez', 8000)
        em_pay = employee.pay
        employee.apply_raise()
        self.assertEqual(employee.pay, int(em_pay * Employee.raise_amt))

    def test_monthly_schedule(self):
        employee = Employee('liana', 'xernez', 8000)
        with patch('tests_simple_employee.requests.get') as mock_requests:
            mock_requests.return_value.ok = True
            self.assertNotEqual(employee.monthly_schedule('january'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
