import sqlite3


db = sqlite3.connect('lab4/database.db')
crs = db.cursor()

try:
    crs.execute('''DROP TABLE PizzaTypes''')
    crs.execute('''DROP TABLE Pizzerias''')
    crs.execute('''DROP TABLE Customers''')
    crs.execute('''DROP TABLE Orders''')
    print('cleared the database')
except:
    print('tables do not exist')

# PizzaTypes
crs.execute('''CREATE TABLE PizzaTypes (
                    type TEXT PRIMARY KEY,
                    price INTEGER,
                    rating REAL,
                    most_sold_at INTEGER
                )''')
crs.execute('''INSERT INTO PizzaTypes VALUES 
                    ('Pesto', 519, 4.9, 6),
                    ('Pepperoni', 469, 4.5, 2),
                    ('Hawaiian', 489, 4.4, 1),
                    ('Margherita', 469, 4.7, 1),
                    ('Dodo', 689, 4.8, 4),
                    ('Arriva', 519, 4.8, 5)''')
crs.execute('''SELECT * FROM PizzaTypes''')
print(crs.fetchall())

# Pizzerias
crs.execute('''CREATE TABLE Pizzerias (
                    id INTEGER PRIMARY KEY,
                    city TEXT,
                    street TEXT,
                    year_opened INTEGER,
                    max_people INTEGER
                )''')
crs.execute('''INSERT INTO Pizzerias VALUES 
                    (NULL, 'SPb', 'Nevsky', 2020, 60),
                    (NULL, 'SPb', 'Kamennoostrovsky', 2019, 70),
                    (NULL, 'Prostokvashino', 'Mira', 2024, 50),
                    (NULL, 'Khimki', 'Voronicyna', 2001, 55),
                    (NULL, 'Prostokvashino', 'Wall Street', 2021, 123),
                    (NULL, 'SPb', 'Chyornaya Rechka', 2018, 65)''')
crs.execute('''SELECT * FROM Pizzerias''')
print(crs.fetchall())

# Customers
crs.execute('''CREATE TABLE Customers (
                    id INTEGER PRIMARY KEY,
                    age INTEGER,
                    fav_pizza TEXT,
                    fav_pizzeria INTEGER
                )''')
crs.execute('''INSERT INTO Customers VALUES 
                    (NULL, 18, 'Pesto', 2),
                    (NULL, 23, 'Dodo', 4),
                    (NULL, 18, 'Pepperoni', 6),
                    (NULL, 2, 'Hawaiian', 3),
                    (NULL, 256, 'Arriva', 5)''')
crs.execute('''SELECT * FROM Customers''')
print(crs.fetchall())


# Orders
crs.execute('''CREATE TABLE Orders (
                    id INTEGER PRIMARY KEY,
                    customer INTEGER,
                    pizzeria INTEGER,
                    pizza_type TEXT,
                    date TEXT
                )''')
crs.execute('''INSERT INTO Orders VALUES 
                    (NULL, 1, 2, 'Pesto', '2023-05-12'),
                    (NULL, 2, 4, 'Dodo', '2022-01-22'),
                    (NULL, 3, 6, 'Pepperoni', '2021-10-04'),
                    (NULL, 4, 1, 'Hawaiian', '2024-01-01'),
                    (NULL, 5, 4, 'Arriva', '2020-02-02'),
                    (NULL, 1, 6, 'Margherita', '2023-06-10'),
                    (NULL, 2, 1, 'Arriva', '2022-11-21'),
                    (NULL, 3, 5, 'Pesto', '2023-12-01'),
                    (NULL, 4, 3, 'Dodo', '2022-09-03'),
                    (NULL, 5, 3, 'Pepperoni', '2021-01-31'),
                    (NULL, 1, 1, 'Pepperoni', '2022-03-24')''')
crs.execute('''SELECT * FROM Orders''')
print(crs.fetchall())

# JOIN query
crs.execute('''SELECT o.id, p.id, o.pizza_type, o.date, p.city, p.street FROM Orders o 
               LEFT JOIN Pizzerias p ON o.pizzeria = p.id''')
print('\n\n')
print(*crs.fetchall(), sep='\n')

# WHERE and GROUP BY query

# Finish run
crs.execute('''DROP TABLE PizzaTypes''')
crs.execute('''DROP TABLE Pizzerias''')
crs.execute('''DROP TABLE Customers''')
crs.execute('''DROP TABLE Orders''')

db.commit()
db.close()