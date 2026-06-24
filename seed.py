import sqlite3
from faker import Faker
import random


def seed_db():
    fake = Faker()

    # 1. Фіксовані статуси за умовою завдання
    statuses = [('new',), ('in progress',), ('completed',)]

    # 2. Генеруємо користувачів
    users = []
    for _ in range(10):
        users.append((fake.name(), fake.unique.email()))

    # 3. Генеруємо завдання
    tasks = []
    for _ in range(25):
        title = fake.sentence(nb_words=4)
        description = fake.text(max_nb_chars=100) if random.choice(
            [True, False]) else None  # Інколи залишаємо пустим за умовою завдання
        status_id = random.randint(1, 3)
        user_id = random.randint(1, 10)
        tasks.append((title, description, status_id, user_id))

    # Запис даних у базу
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()

        # Заповнюємо статуси
        cur.executemany("INSERT INTO status (name) VALUES (?);", statuses)

        # Заповнюємо користувачів
        cur.executemany("INSERT INTO users (fullname, email) VALUES (?, ?);", users)

        # Заповнюємо завдання
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?);", tasks)

        con.commit()
        print("Базу даних успішно заповнено фейковими даними!")


if __name__ == "__main__":
    seed_db()