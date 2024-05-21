output_1 = 'результат операции: 42'
output_2 = 'результат операции: 514'
output_3 = 'результат работы программы: 9'

index_1 = output_1.index('42')
index_2 = output_2.index('514')
index_3 = output_3.index('9')

print(int(output_1[index_1:]) + 10)
print(int(output_2[index_2:]) + 10)
print(int(output_3[index_3:]) + 10)
