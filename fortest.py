note = [
"Имя пользователя",
"Название заметки",
"Содержание Заметки",
["Заголовок1", "Заголовок2", "Заголовок3"]
]

note[0] = input("Введите имя пользователя: ")
note[1] = input("Введите название заметки: ")
note[2] = input("Введите текст заметки: ")
note[3][0] = input("Введите заголовок 1 заметки: ")
note[3][1] = input("Введите заголовок 2 заметки: ")
note[3][2] = input("Введите заголовок 3 заметки: ")




print("Имя пользователя: ", note[0])
print("Название заметки: ", note[1])
print("Содержание Заметки: ", note[2])
print("Заголовок 1 заметки: ",note[3][0])
print("Заголовок 2 заметки: ",note[3][1])
print("Заголовок 3 заметки: ", note[3][2])