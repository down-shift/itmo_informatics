CREATE DATABASE pizza_db_mysql;

CREATE TABLE PizzaTypes (
    type VARCHAR(16) PRIMARY KEY,
    price INT,
    rating FLOAT,
    most_sold_at INT
);

INSERT INTO PizzaTypes VALUES 
    ('Pesto', 519, 4.9, 6),
    ('Pepperoni', 469, 4.5, 2),
    ('Hawaiian', 489, 4.4, 1),
    ('Margherita', 469, 4.7, 1),
    ('Dodo', 689, 4.8, 4),
    ('Arriva', 519, 4.8, 5);
    
-- SELECT * FROM PizzaTypes;

CREATE TABLE Pizzerias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    city VARCHAR(16),
    street VARCHAR(16),
    year_opened INT,
    max_people INT
);

INSERT INTO Pizzerias VALUES 
    (NULL, 'SPb', 'Nevsky', 2020, 60),
    (NULL, 'SPb', 'Kamennoostrovsky', 2019, 70),
    (NULL, 'Prostokvashino', 'Mira', 2024, 50),
    (NULL, 'Khimki', 'Voronicyna', 2001, 55),
    (NULL, 'Prostokvashino', 'Wall Street', 2021, 123),
    (NULL, 'SPb', 'Chyornaya Rechka', 2018, 65);
    
-- SELECT * FROM Pizzerias;

CREATE TABLE Customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    age INT,
    fav_pizza VARCHAR(16),
    fav_pizzeria INT
);

INSERT INTO Customers VALUES 
    (NULL, 18, 'Pesto', 2),
    (NULL, 23, 'Dodo', 4),
    (NULL, 18, 'Pepperoni', 6),
    (NULL, 2, 'Hawaiian', 3),
    (NULL, 256, 'Arriva', 5);
    
-- SELECT * FROM Customers;

CREATE TABLE Orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer INT,
    pizzeria INT,
    pizza_type VARCHAR(16),
    date VARCHAR(16)
);

INSERT INTO Orders VALUES 
    (NULL, 1, 2, 'Pesto', '2023-05-12'),
    (NULL, 2, 4, 'Dodo', '2022-01-22'),
    (NULL, 3, 6, 'Pepperoni', '2021-10-04'),
    (NULL, 4, 1, 'Hawaiian', '2024-01-01'),
    (NULL, 4, 1, 'Hawaiian', '2024-01-01'),
    (NULL, 1, 6, 'Pepperoni', '2022-07-12'),
    (NULL, 5, 4, 'Arriva', '2020-02-02'),
    (NULL, 1, 6, 'Margherita', '2023-06-10'),
    (NULL, 2, 1, 'Arriva', '2022-11-21'),
    (NULL, 3, 5, 'Pesto', '2023-12-01'),
    (NULL, 4, 3, 'Dodo', '2022-09-03'),
    (NULL, 5, 3, 'Pepperoni', '2021-01-31'),
    (NULL, 1, 1, 'Pepperoni', '2022-03-24');
    
-- SELECT * FROM Orders;

SELECT o.customer, p.id, o.pizza_type, o.date, p.city, p.street FROM Orders o 
LEFT JOIN Pizzerias p ON o.pizzeria = p.id;

SELECT customer, COUNT(customer) FROM Orders
WHERE customer != 3
GROUP BY customer
ORDER BY COUNT(customer) DESC;

SELECT * FROM PizzaTypes
WHERE price < (SELECT AVG(price) FROM PizzaTypes)
ORDER BY rating DESC;

SELECT * FROM Orders
WHERE pizza_type IN (SELECT fav_pizza FROM Customers);

SELECT pizza_type FROM Orders UNION SELECT type from PizzaTypes
ORDER BY pizza_type DESC;

SELECT id, fav_pizza FROM Customers UNION ALL 
SELECT customer, pizza_type from Orders
ORDER BY id ASC;

SELECT DISTINCT customer, pizza_type from Orders
ORDER BY customer ASC;

UPDATE Customers SET age = 1024 WHERE age < 14 OR age > 86;
SELECT * FROM Customers;

UPDATE Pizzerias, (SELECT AVG(max_people) AS a FROM Pizzerias) as MeanPeople 
SET max_people = max_people + 5 
WHERE max_people < MeanPeople.a;
SELECT * FROM Pizzerias;

DELETE FROM Orders WHERE date > '2023-12-31';
SELECT * FROM Orders;

DELETE FROM Orders WHERE pizza_type='Dodo';
SELECT * FROM Orders;

DROP TABLE PizzaTypes;
DROP TABLE Pizzerias;
DROP TABLE Customers;
DROP TABLE Orders;
