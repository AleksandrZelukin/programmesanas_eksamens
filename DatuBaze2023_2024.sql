-- 1. Datu bāzes struktūra un izveide
-- Datu bāzi veidojam ar trim tabulām: cafes, employees, un orders, ņemot vērā norādīto informāciju un labās prakses principus.

-- 1.1. Tabulu struktūras apraksts
-- cafes (kafejnīcas):

-- id - primārā atslēga (INTEGER, AUTO_INCREMENT).
-- name - kafejnīcas nosaukums (VARCHAR(100)).
-- address - adrese (VARCHAR(200)).
-- employees (darbinieki):

-- id - primārā atslēga (INTEGER, AUTO_INCREMENT).
-- first_name - vārds (VARCHAR(50)).
-- last_name - uzvārds (VARCHAR(50)).
-- phone_number - tālruņa numurs (VARCHAR(15)).
-- position - amats (VARCHAR(50)).
-- cafe_id - ārējā atslēga uz cafes.id (INTEGER).
-- on_vacation - vai atvaļinājumā (BOOLEAN).
-- orders (pasūtījumi):

-- id - primārā atslēga (INTEGER, AUTO_INCREMENT).
-- amount - pasūtījuma summa (DECIMAL(10, 2)).
-- order_date - datums (DATE).
-- description - apraksts (TEXT).
-- employee_id - ārējā atslēga uz employees.id (INTEGER).
-- 1.2. Relāciju apraksts
-- employees.cafe_id ir ārējā atslēga, kas sasaista katru darbinieku ar konkrētu kafejnīcu.
-- orders.employee_id ir ārējā atslēga, kas sasaista katru pasūtījumu ar darbinieku, kas to veicis.


-- 1.3. SQL datu bāzes izveide un datu ievade

-- 1. Tabulas izveide kafejnīcām
CREATE TABLE cafes (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL
);

-- 2. Tabulas izveide darbiniekiem
CREATE TABLE employees (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15),
    position VARCHAR(50),
    cafe_id INTEGER,
    on_vacation BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (cafe_id) REFERENCES cafes(id)
);

-- 3. Tabulas izveide pasūtījumiem
CREATE TABLE orders (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    order_date DATE NOT NULL,
    description TEXT,
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Datu ievade tabulās
INSERT INTO cafes (name, address) VALUES
    ('Pie Jāņa', 'Brīvības iela 10'),
    ('Kafe Lat', 'Kalnciema iela 2'),
    ('Rīts un Vakars', 'Maskavas iela 50');

INSERT INTO employees (first_name, last_name, phone_number, position, cafe_id, on_vacation) VALUES
    ('Jānis', 'Bērziņš', '+37120000000', 'viesmīlis', 1, TRUE),
    ('Anna', 'Kalniņa', '+37121111111', 'pavārs', 2, FALSE),
    ('Mārtiņš', 'Ozols', '+37122222222', 'menedžeris', 1, FALSE);

INSERT INTO orders (amount, order_date, description, employee_id) VALUES
    (249.99, '2024-04-01', 'Produkti atvēršanai', 1),
    (150.50, '2024-04-02', 'Kafijas pupiņas', 3),
    (89.99, '2024-04-03', 'Cepumu iepakojums', 2);


-- 1. Datu bāzes struktūra un izveide
-- Datu bāzi veidojam ar trim tabulām: cafes, employees, un orders, ņemot vērā norādīto informāciju un labās prakses principus.

-- 1.1. Tabulu struktūras apraksts
-- cafes (kafejnīcas):

-- id - primārā atslēga (INTEGER, AUTO_INCREMENT).
-- name - kafejnīcas nosaukums (VARCHAR(100)).
-- address - adrese (VARCHAR(200)).
-- employees (darbinieki):

-- id - primārā atslēga (INTEGER, AUTO_INCREMENT).
-- first_name - vārds (VARCHAR(50)).
-- last_name - uzvārds (VARCHAR(50)).
-- phone_number - tālruņa numurs (VARCHAR(15)).
-- position - amats (VARCHAR(50)).
-- cafe_id - ārējā atslēga uz cafes.id (INTEGER).
-- on_vacation - vai atvaļinājumā (BOOLEAN).
-- orders (pasūtījumi):

-- id - primārā atslēga (INTEGER, AUTO_INCREMENT).
-- amount - pasūtījuma summa (DECIMAL(10, 2)).
-- order_date - datums (DATE).
-- description - apraksts (TEXT).
-- employee_id - ārējā atslēga uz employees.id (INTEGER).
-- 1.2. Relāciju apraksts
-- employees.cafe_id ir ārējā atslēga, kas sasaista katru darbinieku ar konkrētu kafejnīcu.
-- orders.employee_id ir ārējā atslēga, kas sasaista katru pasūtījumu ar darbinieku, kas to veicis.
-- 1.3. SQL datu bāzes izveide un datu ievade

-- 1. Tabulas izveide kafejnīcām

CREATE TABLE cafes (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL
);

-- 2. Tabulas izveide darbiniekiem
CREATE TABLE employees (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15),
    position VARCHAR(50),
    cafe_id INTEGER,
    on_vacation BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (cafe_id) REFERENCES cafes(id)
);

-- 3. Tabulas izveide pasūtījumiem
CREATE TABLE orders (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    order_date DATE NOT NULL,
    description TEXT,
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Datu ievade tabulās
INSERT INTO cafes (name, address) VALUES
    ('Pie Jāņa', 'Brīvības iela 10'),
    ('Kafe Lat', 'Kalnciema iela 2'),
    ('Rīts un Vakars', 'Maskavas iela 50');

INSERT INTO employees (first_name, last_name, phone_number, position, cafe_id, on_vacation) VALUES
    ('Jānis', 'Bērziņš', '+37120000000', 'viesmīlis', 1, TRUE),
    ('Anna', 'Kalniņa', '+37121111111', 'pavārs', 2, FALSE),
    ('Mārtiņš', 'Ozols', '+37122222222', 'menedžeris', 1, FALSE);

INSERT INTO orders (amount, order_date, description, employee_id) VALUES
    (249.99, '2024-04-01', 'Produkti atvēršanai', 1),
    (150.50, '2024-04-02', 'Kafijas pupiņas', 3),
    (89.99, '2024-04-03', 'Cepumu iepakojums', 2);
-- 2. SQL vaicājumi
-- 2.1. Darbinieki, kas pašlaik ir atvaļinājumā.
SELECT first_name, last_name, position 
FROM employees 
WHERE on_vacation = TRUE;

-- 2.2. Pasūtījumu kopējais skaits.

SELECT COUNT(*) AS total_orders 
FROM orders;

-- 2.3. Katra darbinieka pasūtījumu kopējais skaits.
SELECT e.first_name, e.last_name, COUNT(o.id) AS total_orders 
FROM employees e
LEFT JOIN orders o ON e.id = o.employee_id
GROUP BY e.id;

-- 2.4. Katra darbinieka pasūtījumu vislielākā summa.

SELECT e.first_name, e.last_name, MAX(o.amount) AS max_order_amount 
FROM employees e
LEFT JOIN orders o ON e.id = o.employee_id
GROUP BY e.id;

-- 2.5. Katras kafejnīcas pasūtījumu vidējā summa.

SELECT c.name AS cafe_name, AVG(o.amount) AS average_order_amount
FROM cafes c
LEFT JOIN employees e ON c.id = e.cafe_id
LEFT JOIN orders o ON e.id = o.employee_id
GROUP BY c.id;