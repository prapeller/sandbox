f = open('1_file.txt', 'w', encoding='utf-8')

while True:
    data = input('enter line to write into file or press "Enter" to exit > ')
    if data == '':
        break
    f.write(data + '\n')

f.close()
