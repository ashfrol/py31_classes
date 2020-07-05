from datetime import date

from accounting.application.db.people import get_employees
from accounting.application.salary import calculate_salary

if __name__ == '__main__':
    person = 'Bill'
    company = 'Versal'
    calculate_salary(person=person)
    get_employees(company=company)
    print(date.today())