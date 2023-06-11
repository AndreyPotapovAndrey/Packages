from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    calculate_salary(50000, 20000)
    get_employees('Антон', 'Георгий', 'Мария')
print(datetime.date.today())




