# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять
# сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.

matrix = []

for i in range(4):
    matrix.append([])
    j_sum = 0
    for j in range(5):
        if j < 4:
            n = int(input('enter number: '))
            matrix[i].append(n)
            j_sum += n
        else:
            matrix[i].append(j_sum)

for line in matrix:
    for n in line:
        print(f'{n:>5}', end='')
    print()
