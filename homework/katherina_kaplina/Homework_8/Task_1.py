import random

user_salary = int(input("What is your salary in $: "))
user_bonus = random.choice([True, False])

if user_bonus:
    user_money = user_salary + int(random.random() * 100)
else:
    user_money = user_salary

print(f'Your final salary will be: {user_money}')
