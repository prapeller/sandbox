import pickle
import json

my_favourite_group = {
    1: 'hello', 2: "привет", 3: '你好',
    'age': [3, 34, 25]
}

json_my_favourite_group = json.dumps(my_favourite_group)
print(json_my_favourite_group, type(json_my_favourite_group))

p_group = pickle.dumps(my_favourite_group)
print(p_group, type(p_group))

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
