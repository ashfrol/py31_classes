from datetime import date

from accounting import *

if __name__ == '__main__':
    person = 'Bill'
    company = 'Versal'
    calculate_salary(person=person)
    get_employees(company=company)
    print(date.today())