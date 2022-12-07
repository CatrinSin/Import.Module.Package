from application.salary import calculate_salary
from application.db.people import get_employees
from numerology import Pythagorean
from pprint import pprint
from datetime import datetime

def get_numerology():
    name = input("Insert your name: ")
    sec_name = input("Insert your surname: ")
    date_of_birth = input("Insert your birthdate in format yyyy-mm-dd: ")
    num = Pythagorean(first_name=name, last_name=sec_name, birthdate=date_of_birth, verbose=False)
    pprint(num.interpretations)

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    # get_numerology()
    print(datetime.today())

