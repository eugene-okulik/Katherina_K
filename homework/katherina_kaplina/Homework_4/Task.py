my_dict = {
    'tuple': (1, 'text', 4.8, True, 122),
    'list': [1, 2, 3, 4, 5, 6],
    'dict': {
        'one': 'banana',
        'two': 'kiwi',
        'three': 'apple',
        'four': 'grape',
        'five': 'blueberry'
    },
    'set': {1, 'New York', 2, 'London', 3, 'Brasilia'}
}

print(my_dict['tuple'][-1])
my_dict['list'].append('last element')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = (1, 2, 3)
my_dict['dict'].pop('one')
my_dict['set'].add('Milan')
my_dict['set'].pop()
print(my_dict)
