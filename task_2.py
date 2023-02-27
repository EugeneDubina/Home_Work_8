count_line = 0
count_words = 0
count_symbols = 0

with open('task_8_2.txt', 'r', encoding='utf-8') as text:
    for line in text:
        print()
        count_line += 1
        count_words = len(line.split())
        print(f'количество слов в строке "{line}" = {count_words}')
        print()
        for el in line.split():
            count_symbols = len(el.strip('\n'))
            print(f'количество символов в слове "{el}" = {count_symbols}')
    print()
    print(f'количество строк в тексте {count_line}')