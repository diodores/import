import datetime
from salary import *
from people import *

if __name__ == '__main__':
    print(f'Текущая дата: {datetime.datetime.now()}')
    calculate_salary()
    get_employees()
    print("Программа завершена.")