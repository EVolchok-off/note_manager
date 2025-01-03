note = [
    "Имя пользователя",
    "Содержание заметки",
    "Статус",
    "Дата создания",
    "Дата изменения",
    ["Заголовок 1", "Заголовок 2", "Заголовок 3"]  # вложенный список для заголовков
]

note[0] = input("Введите имя пользователя: ")
note[5][0] = input("Введите первый заголовок заметки: ")
note[5][1] = input("Введите второй заголовок заметки: ")
note[5][2] = input("Введите третий заголовок заметки: ")
note[1] = input("Введите текст заметки: ")
note[2] = input("Введите статус заметки: ")
note[3] = input("Введите дату создания заметки (в виде хх.хх.хххх): ")
note[4] = input("Введите дату истечения заметки (в виде хх.хх.хххх): ")


import re

temp_created_date = re.split(r'[,.\n? -]+', note[3])
temp_issue_date = re.split(r'[,.\n? -]+', note[4])

print("Имя пользователя:", note[0])
print("Первый заголовок заметки: ", note[5][0])
print("Второй заголовок заметки: ", note[5][1])
print("Третий заголовок заметки: ", note[5][2])
print("Текст заметки:", note[1])
print("Статус заметки:", note[2])
print("Дата создания заметки:", str(temp_created_date[0] + ' - ' + temp_created_date[1]))
print("Дата истечения заметки:", str(temp_issue_date[0] + ' - ' + temp_issue_date[1]))
