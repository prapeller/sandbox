class Worker:
    name = str()
    surname = str()
    position = str()
    _income = dict()

    def __init__(self, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


# https://www.bbc.com/russian/russia/2015/05/150505_sechin_salary_rosneft
# https://www.bbc.com/russian/news-49979517
# https://www.youtube.com/watch?v=ipAnwilMncI
rosneft_president = Position(20_000_000, 30_000_000)
russia_president = Position(773_400, 100_000_000_000)

rosneft_president.name, rosneft_president.surname = ('Gangster', 'Sechin')
russia_president.name, russia_president.surname = ('Gangster', 'Putin')

print(f'{rosneft_president.get_full_name()} total income: {rosneft_president.get_total_income()}')
print(f'{russia_president.get_full_name()} total income: {russia_president.get_total_income()}')
