PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = PRICE_LIST.split('\n')

my_dict = {i.split()[0]: int(i.split()[1][:-1]) for i in my_list}

print(my_dict)
