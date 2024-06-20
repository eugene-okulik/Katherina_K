import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(csv_file_path, 'r') as file:
    file_data = csv.DictReader(file)
    csv_data = [line for line in file_data]

cursor = db.cursor(dictionary=True)
query = '''
select s.name, s.second_name, `groups`.title as group_title, b.title as book_title,
s2.title as subject_title, l.title as lesson_title, m.value as mark_value
from students s
join `groups` on s.group_id = `groups`.id
join books b on s.id = b.taken_by_student_id
join marks m on s.id = m.student_id
join lessons l on m.lesson_id = l.id
join subjets s2 on l.subject_id  = s2.id
'''

cursor.execute(query)
db_results = cursor.fetchall()

no_in_db_results = []
for i in csv_data:
    if i not in db_results:
        no_in_db_results.append(i)
    else:
        pass

for row in no_in_db_results:
    print(row)

db.commit()

db.close()
