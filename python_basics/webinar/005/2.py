with open('2_file.txt', encoding='utf-8') as f:
    lineslist = f.readlines()

    print(f'total lines: {len(lineslist)} \n')

    lines_counter = 1

    for line in lineslist:
        line = line.replace('\n', '')
        if line != '':
            words_qty = len(line.split(' '))
        else:
            words_qty = 0

        print(f'line {lines_counter}: {words_qty} word(s)')
        lines_counter += 1
