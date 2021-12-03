# 1
result = int(input("enter number here > "))
print(result + 2)

# 2
while True:
    number = int(input("enter 0 < number < 10... "))
    if (0 < number) and (number < 10):
        print('number^2: ', number ** 2)
        break
    elif number < 0:
        print("should be number > 0")
    elif number > 10:
        print("should be number < 10")

# 3


class User:

    def __init__(self):
        self.first_name = input('enter your first name > ')
        self.last_name = input('enter your last name > ')
        self.age = int(input('enter your age > '))
        self.weight = int(input('enter your weight > '))

    def __str__(self):
        result = f'{self.first_name} {self.last_name}, age = {self.age}, weight = {self.weight}'
        return result

    def get_recommendations(self):
        if self.age > 40 and (self.weight < 50 or self.weight > 120):
            return f'{self.first_name} {self.last_name}, you should visit doctor!'
        elif self.age > 30 and (self.weight < 50 or self.weight > 120):
            return f'{self.first_name} {self.last_name}, you should pay more attention to your age and weight balance!'
        else:
            return f'{self.first_name} {self.last_name}, your age and weight balance is OK!'


user_1 = User()
print(user_1.get_recommendations())
