import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


create_table_countries = '''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);
'''

conn.execute(create_table_countries)
conn.commit()


def additions_countries():
    insert_countries = '''
    INSERT INTO countries (title)
    VALUES (?);
    '''
    countries = [
        ('Kyrgyzstan',),
        ('Germany',),
        ('China',)
    ]
    cursor.executemany(insert_countries, countries)
    conn.commit()

additions_countries()

create_table_cities = '''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area TEXT DEFAULT '0',
    country_id INTEGER REFERENCES countries(id)
);
'''

conn.execute(create_table_cities)
conn.commit()

def additions_cities():
    insert_cities = '''
    INSERT INTO cities (title, area, country_id)
    VALUES (?, ?, ?);
    '''
    cities = [
        ('Bishkek', '127 км²', 1),
        ('Berlin', '891,8 км²', 2),
        ('Pekin', '16 411 км²', 3),
        ('Osh', '182 км²', 1),
        ('Zhengzhou', '7 567 км²', 3),
        ('Munich', '310,7 км²', 2),
        ('Hamburg', '755,2 км²', 2)
    ]
    cursor.executemany(insert_cities, cities)
    conn.commit()

additions_cities()

create_table_employees = '''
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER INTEGER REFERENCES cities(id)
    );
    '''
conn.execute(create_table_employees)
conn.commit()

def additions_emploees():
    insert_employees = '''
    INSERT INTO employees (first_name, last_name, city_id)
    VALUES (?, ?, ?);
    '''
    employees = [
    ("Hans", "Müller", 2),
    ("Frieda", "Schmidt", 2),
    ("Klaus", "Fischer", 1),
    ("Greta", "Koch", 8),
    ("Heinrich", "Schneider", 7),
    ("Иван", "Иванов", 3),
    ("Мария", "Петрова", 1),
    ("Алексей", "Смирнов", 4),
    ("Павел", "Федоров", 6),
    ("Wei", "Wang", 3),
    ("Li", "Li", 5),
    ("Chen", "Zhang", 1),
    ("Yan", "Liu", 7),
    ("Jing", "Chen", 4)
]

    cursor.executemany(insert_employees, employees)
    conn.commit()

additions_emploees()


def list_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]} - {city[1]}")

def employees_in_city(city_id):
    join_f = '''
    SELECT e.first_name, e.last_name, c.title AS city_name, c.area, co.title AS country_name
    FROM employees e
    JOIN cities c ON e.city_id = c.id
    JOIN countries co ON c.country_id = co.id
    WHERE c.id = ?
    '''
    cursor.execute(join_f, (city_id,))
    employees = cursor.fetchall()
    for employee in employees:
        print(f"ИМЯ: {employee[0]}, ФАМИЛИЯ: {employee[1]}, ГОРОД: {employee[2]}, ПЛОЩАДЬ: {employee[3]}, СТРАНА: {employee[4]}")


while 1:
    print("Вы можете отобразить список сотрудников по выбранному id города")
    print("Из перечня городов ниже:")
    list_cities()

    input_id = int(input("Введите id города (для выхода из программы введите 0): "))

    if input_id == 0:
        break

    employees_in_city(input_id)

conn.close()