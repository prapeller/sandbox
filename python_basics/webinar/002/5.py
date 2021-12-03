my_list = [7, 5, 3, 3, -3]
while True:
    try:
        user_number = int(input('enter number for adding to list > '))
        break
    except ValueError as e:
        continue

inverted_list = my_list[::-1]

for index, number in enumerate(inverted_list, 0):
    if index == len(inverted_list) - 1 and user_number > number:
        inverted_list.append(user_number)
        break

    if user_number > number:
        continue
    else:
        inverted_list.insert(index, user_number)
        break

my_list = inverted_list[::-1]
print(my_list)
