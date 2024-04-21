import os
import json
from datetime import datetime

NOTES_FILE = "заметки.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

def create_note():
    title = input("Введите название заметки: ")
    content = input("Введите содержимое заметки: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"Название": title, "Содержание": content, "Дата создания": created_at}
    notes.append(note)
    save_notes(notes)

def edit_note():
    title_or_date = input("Введите название или дату создания заметки для редактирования: ")
    for note in notes:
        if title_or_date.lower() in [note["Название"].lower(), note["Дата создания"]]:
            new_content = input("Введите новое содержимое заметки: ")
            note["Содержание"] = new_content
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка не найдена.")

def read_note():
    title_or_date = input("Введите название или дату создания заметки для прочтения: ")
    for note in notes:
        if title_or_date.lower() in [note["Название"].lower(), note["Дата создания"]]:
            print(f"Название: {note['Название']}\nСодержание: {note['Содержание']}\nДата создания: {note['Дата создания']}")
            return
    print("Заметка не найдена.")

def delete_note():
    title_or_date = input("Введите название или дату создания заметки для удаления: ")
    for note in notes:
        if title_or_date.lower() in [note["Название"].lower(), note["Дата создания"]]:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка не найдена.")

def filter_notes_by_date():
    date_filter = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    filtered_notes = [note for note in notes if note["Дата создания"].startswith(date_filter)]
    if filtered_notes:
        print("Отфильтрованные заметки:")
        for note in filtered_notes:
            print(f"Название: {note['Название']}, Дата создания: {note['Дата создания']}")
    else:
        print("Заметки по указанной дате не найдены.")

if __name__ == "__main__":
    notes = load_notes()
    
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Редактировать заметку")
        print("3. Прочитать заметку")
        print("4. Удалить заметку")
        print("5. Фильтровать заметки по дате создания")
        print("6. Выйти")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            read_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            filter_notes_by_date()
        elif choice == "6":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")