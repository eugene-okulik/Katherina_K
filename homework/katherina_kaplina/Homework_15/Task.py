import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

query = "insert into students (name, second_name) values ( %s,  %s)"
cursor.execute(query, ('Kate', 'Petrova234567'))
student_id = cursor.lastrowid

query = "insert into books (title, taken_by_student_id) values ('algebra_1', %s)"
cursor.execute(query, (student_id,))
query = "insert into books (title, taken_by_student_id) values ('algebra_2', %s)"
cursor.execute(query, (student_id,))
query = "insert into books (title, taken_by_student_id) values ('algebra_3', %s)"
cursor.execute(query, (student_id,))

query = "insert into `groups` (title, start_date, end_date) values (%s, %s, %s)"
cursor.execute(query, ('third', 'sept 2023', 'may 2024'))
group_id_my = cursor.lastrowid

query = "update students set group_id = %s where id = %s"
cursor.execute(query, (group_id_my, student_id))

query = "insert into subjets (title) values (%s)"
cursor.execute(query, ('mathematics_1',))
subject_id_1 = cursor.lastrowid
query = "insert into subjets (title) values (%s)"
cursor.execute(query, ('chemistry_1',))
subject_id_2 = cursor.lastrowid

query = "insert into lessons (title, subject_id) values ('mathematics_11', %s)"
cursor.execute(query, (subject_id_1,))
lesson_id_11 = cursor.lastrowid
query = "insert into lessons (title, subject_id) values ('mathematics_22', %s)"
cursor.execute(query, (subject_id_1,))
lesson_id_12 = cursor.lastrowid
query = "insert into lessons (title, subject_id) values ('liter_11', %s)"
cursor.execute(query, (subject_id_2,))
lesson_id_21 = cursor.lastrowid
query = "insert into lessons (title, subject_id) values ('liter_22', %s)"
cursor.execute(query, (subject_id_2,))
lesson_id_22 = cursor.lastrowid

query = "insert into marks (value , lesson_id, student_id) values ('very bad', %s, %s)"
cursor.execute(query, (lesson_id_11, student_id))
query = "insert into marks (value , lesson_id, student_id) values ('not so bad', %s, %s)"
cursor.execute(query, (lesson_id_12, student_id))
query = "insert into marks (value , lesson_id, student_id) values ('very bad', %s, %s)"
cursor.execute(query, (lesson_id_21, student_id))
query = "insert into marks (value , lesson_id, student_id) values ('good', %s, %s)"
cursor.execute(query, (lesson_id_22, student_id))

query = "select * from marks where student_id = %s"
cursor.execute(query, (student_id,))
results_1 = cursor.fetchall()
for row in results_1:
    print(row)

query = "select * from books where taken_by_student_id = %s"
cursor.execute(query, (student_id,))
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
