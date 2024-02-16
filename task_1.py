import pandas as pd
import datetime

# Функция для создания новой заметки
def create_note():
    note_id = len(df) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = (datetime.datetime.now()).strftime('%d.%m.%Y  %H:%M:%S')
    new_note = {'id': note_id, 'Заголовок': title, 'Текст заметки': body, 'Дата создания': timestamp}
    df.loc[len(df)] = new_note
    print("Заметка успешно создана!")

# Функция для чтения всех заметок
def read_notes():
    print(df)

# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    if note_id in df['id'].values:

        print("Выберите, что вы хотите изменить:")
        print("1. Заголовок")
        print("2. Тело")
        print("3. И заголовок, и тело")
        choice = input("Ваш выбор: ")

        if choice == '1':
            new_title = input("Введите новый заголовок заметки: ")
            df.loc[df['id'] == note_id, 'Заголовок'] = new_title
            print("Заголовок успешно отредактирован!")
        elif choice == '2':
            new_body = input("Введите новое тело заметки: ")
            df.loc[df['id'] == note_id, 'Текст заметки'] = new_body
            print("Тело успешно отредактировано!")
        elif choice == '3':
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            df.loc[df['id'] == note_id, ['Заголовок', 'Текст заметки']] = [new_title, new_body]
            print("Заголовок и тело успешно отредактированы!")
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
    else:
        print("Заметка с таким ID не найдена.")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    if note_id in df['id'].values:
        df.drop(df[df['id'] == note_id].index, inplace=True)
        print("Заметка успешно удалена!")
    else:
        print("Заметка с таким ID не найдена.")

# Загрузка заметок из CSV файла (если он существует)
try:
    df = pd.read_csv('notes.csv', sep=';')
except FileNotFoundError:
    df = pd.DataFrame(columns=['id', 'Заголовок', 'Текст заметки', 'Дата создания'])

# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Создать новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        create_note()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        df.to_csv('notes.csv', sep=';', index=False)
        print("Заметки сохранены в файл notes.csv. До свидания!")
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
