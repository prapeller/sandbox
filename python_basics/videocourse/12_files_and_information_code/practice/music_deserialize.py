import json
import pickle

with open('group.json', 'r') as f:
    dict_from_json = json.load(f)
print(dict_from_json, type(dict_from_json))

with open('group.pickle', 'rb') as f:
    dict_from_pickle = pickle.load(f)
print(dict_from_json, type(dict_from_json))

