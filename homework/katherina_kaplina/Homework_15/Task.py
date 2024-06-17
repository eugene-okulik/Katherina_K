import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("insert into `groups` (title, start_date, end_date) values ('third', 'sept 2023', 'may 2024')")

group_id_my = cursor.lastrowid

cursor.execute(f"insert into students (name, second_name, group_id) values ('Kate', 'Petrova', {group_id_my})")
student_id = cursor.lastrowid

cursor.execute(f"insert into books (title, taken_by_student_id) values ('algebra_1', {student_id})")
cursor.execute(f"insert into books (title, taken_by_student_id) values ('algebra_2', {student_id})")
cursor.execute(f"insert into books (title, taken_by_student_id) values ('algebra_3', {student_id})")

cursor.execute("insert into subjets (title) values ('mathematics_1')")
subject_id_1 = cursor.lastrowid
cursor.execute("insert into subjets (title) values ('chemistry_1')")
subject_id_2 = cursor.lastrowid

cursor.execute(f"insert into lessons (title, subject_id) values ('mathematics_11', {subject_id_1})")
lesson_id_11 = cursor.lastrowid
cursor.execute(f"insert into lessons (title, subject_id) values ('mathematics_22', {subject_id_1})")
lesson_id_12 = cursor.lastrowid
cursor.execute(f"insert into lessons (title, subject_id) values ('liter_11', {subject_id_2})")
lesson_id_21 = cursor.lastrowid
cursor.execute(f"insert into lessons (title, subject_id) values ('liter_22', {subject_id_2})")
lesson_id_22 = cursor.lastrowid

cursor.execute(f"insert into marks (value , lesson_id, student_id) values ('very bad', {lesson_id_11}, {student_id})")
cursor.execute(f"insert into marks (value , lesson_id, student_id) values ('not so bad', {lesson_id_12}, {student_id})")
cursor.execute(f"insert into marks (value , lesson_id, student_id) values ('bad', {lesson_id_21}, {student_id})")
cursor.execute(f"insert into marks (value , lesson_id, student_id) values ('bad', {lesson_id_22}, {student_id})")

cursor.execute(f'select * from marks where student_id = {student_id}')
results_1 = cursor.fetchall()
for row in results_1:
    print(row)

cursor.execute(f'select * from books where taken_by_student_id = {student_id}')
results_2 = cursor.fetchall()
for row in results_2:
    print(row)

query = '''
    select s.name, s.second_name, b.title, m.value, l.title, s2.title
    from students s
    join books b on s.id = b.taken_by_student_id
    join marks m on s.id = m.student_id
    join lessons l on m.lesson_id = l.id
    join subjets s2 on l.subject_id  = s2.id
    where s.id = %s
'''
cursor.execute(query, (student_id,))
results_3 = cursor.fetchall()
for row in results_3:
    print(row)

db.commit()

db.close()
