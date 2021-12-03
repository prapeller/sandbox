elements_list = [
    1,
    2.0,
    'three',
    True,
    ['this', 'is', 'list'],
    ('this', 'is', 'tuple'),
    {'this', 'is', 'set'},
    {1: 'this', 2: 'is', 3: 'dictionary'}
]

for element in elements_list:
    print(type(element))
