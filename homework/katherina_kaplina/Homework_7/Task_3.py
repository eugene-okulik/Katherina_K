output_1 = 'результат операции: 42'
output_2 = 'результат операции: 514'
output_3 = 'результат работы программы: 9'
output_4 = 'результат: 2'

def calculation(parameter):
    number = int(parameter.split(': ')[1])
    return number + 10

print(calculation(output_1))
print(calculation(output_2))
print(calculation(output_3))
print(calculation(output_4))
