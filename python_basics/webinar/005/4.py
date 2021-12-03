from googletrans import Translator

translator = Translator()
translated_lines = []

with open('4_original.txt', 'r', encoding='utf-8') as f:
    origin_lines = f.readlines()
    for line in origin_lines:
        line.replace('\n', '')
        translated_line = translator.translate(line, dest='ru').text
        translated_lines.append(translated_line + '\n')

with open('4_translated.txt', 'w', encoding='utf-8') as f:
    f.writelines(translated_lines)
