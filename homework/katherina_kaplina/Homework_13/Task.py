import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            yield line


for data_line in read_file():
    date = data_line[3:29]
    python_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    if data_line[0] == '1':
        time_1 = python_date + datetime.timedelta(days=7)
        print(f"{time_1} is the date 7 days greater than {python_date} date")
    elif data_line[0] == '2':
        time_2 = python_date.strftime('%A')
        print(f"{time_2} is the day of the week for the date {python_date}")
    elif data_line[0] == '3':
        time_3 = datetime.datetime.now() - python_date
        print(f"{time_3.days} days from date {python_date}")
    else:
        pass
