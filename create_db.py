import sqlite3

def create_db():
    # Зчитуємо SQL-скрипт
    with open('tasks.sql', 'r', encoding='utf-8') as f:
        sql = f.read()

    # Створюємо підключення та виконуємо скрипт
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.executescript(sql)
        print("Базу даних 'tasks.db' та таблиці успішно створено!")

if __name__ == "__main__":
    create_db()