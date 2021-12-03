import sys
print(sys.executable)
print(sys.platform)

# 1
def user_to_string(name, age, city):
    return f'{name}, {age} год, проживает в городе {city}'


print(user_to_string('Vasya', 21, 'Moscow'))


# 2
def max_of_3(number_1, number_2, number_3):
    return max(number_1, number_2, number_3)


print(max_of_3(1, 2, 3))

# 3
player = {
    'name': input('player name > '),
    'health': 100,
    'damage': 30,
    'armor': 1.2
}

enemy = {
    'name': input('enemy name > '),
    'health': 70,
    'damage': 20,
    'armor': 1
}


def attack(one, another):
    damage = get_damage(one["damage"], another["armor"])
    print(f'{one["name"]} is attacking {another["name"]}')
    another['health'] -= damage


def get_damage(damage, armor):
    return damage / armor


print('before fight:')
print(player)
print(enemy)

attack(player, enemy)
attack(enemy, player)
attack(enemy, player)
attack(enemy, player)
attack(enemy, player)
attack(enemy, player)
attack(player, enemy)
attack(player, enemy)

print('after fight:')
print(player)
print(enemy)
