output_1 = 'результат операции: 42'
output_2 = 'результат операции: 514'
output_3 = 'результат работы программы: 9'

index_1 = output_1.index(':')
index_2 = output_2.index(':')
index_3 = output_3.index(':')

print(int(output_1[index_1 + 1:]) + 10)
print(int(output_2[index_2 + 1:]) + 10)
print(int(output_3[index_3 + 1:]) + 10)
