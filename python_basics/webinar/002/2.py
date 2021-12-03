items_list = input('enter numbers dividing by " " > ').split()
print(items_list)

for i in range(1, len(items_list), 2):
    items_list.insert(i - 1, items_list.pop(i))

print(items_list)

odd_items_list = items_list[::2]
even_items_list = items_list[1::2]

shifted_list = []
for i in range(len(odd_items_list)):
    try:
        shifted_list.append(even_items_list[i])
    except IndexError as e:
        pass

    shifted_list.append(odd_items_list[i])

print(shifted_list)
