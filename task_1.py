with open('text.txt', 'w', encoding='utf-8') as text:
    while True:
        line = input("Введите данные в строку: ")
        if line == '':
            break
        else:
            text.write(f'{line}\n')