a = 2
b = 3
count = 1

while a < b:
    print(f"{count}-й день: {a:.2f} км")
    a *= 1.1
    count += 1
else:
    print(f'{count}-й день: {a:.2f} км')
    print(f'Ответ: на {count}-й день спортспен достиг результата - не менее {b} км.')
