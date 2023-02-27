eng_origin = ["One", "Two", "Three", "Four"]
rus_translate = ["Один", "Два", "Три", "Четырке"]

with open('task_8_3.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
    for i, word in enumerate(eng_origin):
        if word in data:
            data = data.replace(word, rus_translate[i])
    print(data)
with open('task_8_3_1.txt', 'w', encoding='utf-8') as file:
    file.write(data)