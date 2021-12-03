list_1 = ['1', '2', '3', '4', '5', 6, 7]
list_2 = ['1', '4', 6, 9]

list_1_and_2 = [obj for obj in list_1 if obj in list_2]
print(list_1_and_2)