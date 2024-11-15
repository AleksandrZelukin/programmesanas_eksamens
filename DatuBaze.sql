-- Tabulu struktūra
-- 1. Clients (Klienti)
-- Saglabā informāciju par klientiem.

-- ID (Primary Key) – unikāls klienta identifikators.
-- Name – klienta vārds un uzvārds.
-- PhoneNumber – klienta tālruņa numurs.
-- Email – klienta e-pasta adrese.
-- Address – klienta adrese.
-- 2. Farmers (Saimnieki)
-- Saglabā informāciju par saimniekiem, ar kuriem veikals sadarbojas.

-- ID (Primary Key) – unikāls saimnieka identifikators.
-- Name – saimnieka vārds un uzvārds.
-- PhoneNumber – saimnieka tālruņa numurs.
-- FarmName – saimniecības nosaukums.
-- Location – saimniecības atrašanās vieta.
-- 3. Products (Produkti)
-- Saglabā informāciju par piedāvātajiem produktiem.

-- ID (Primary Key) – unikāls produkta identifikators.
-- Name – produkta nosaukums (piem., „Govs siers svaigs”).
-- Unit – mērvienība (litrs, kilograms, grams).
-- PricePerUnit – cena par vienību (piem., 1,50 €/litrā).
-- FarmerID (Foreign Key) – atsauce uz tabulu Farmers, norādot produkta piegādātāju.
-- 4. Purchases (Iepirkumi)
-- Saglabā informāciju par klientu veiktajiem iepirkumiem.

-- ID (Primary Key) – unikāls iepirkuma identifikators.
-- ClientID (Foreign Key) – atsauce uz tabulu Clients.
-- ProductID (Foreign Key) – atsauce uz tabulu Products.
-- Quantity – iepirktais daudzums (piem., 2 litri vai 1 kilograms).
-- TotalPrice – kopējā cena (PricePerUnit × Quantity).
-- PurchaseDate – datums, kad iepirkums notika.
-- Datu savstarpējās saites
-- Tabula Clients ir saistīta ar Purchases (klienta pirkumi).
-- Tabula Farmers ir saistīta ar Products (saimnieki piegādā produktus).
-- Tabula Products ir saistīta ar Purchases (produktus pērk klienti).
-- SQL Datu Bāzes Veidošana:

CREATE TABLE Clients (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(200)
);

CREATE TABLE Farmers (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    PhoneNumber VARCHAR(20),
    FarmName VARCHAR(100),
    Location VARCHAR(200)
);

CREATE TABLE Products (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Unit VARCHAR(20),
    PricePerUnit DECIMAL(10, 2),
    FarmerID INT,
    FOREIGN KEY (FarmerID) REFERENCES Farmers(ID)
);

CREATE TABLE Purchases (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT,
    ProductID INT,
    Quantity DECIMAL(10, 2),
    TotalPrice DECIMAL(10, 2),
    PurchaseDate DATE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ID),
    FOREIGN KEY (ProductID) REFERENCES Products(ID)
);


INSERT INTO Farmers (Name, PhoneNumber, FarmName, Location)
VALUES ('Jānis Bērziņš', '29123456', 'Zelta Govs', 'Tukuma novads');

INSERT INTO Products (Name, Unit, PricePerUnit, FarmerID)
VALUES ('Govs piens 2%', 'Litrs', 1.32, 1);

INSERT INTO Clients (Name, PhoneNumber, Email, Address)
VALUES ('Anna Liepa', '29456789', 'anna.liepa@example.com', 'Rīga, Brīvības iela 10');

INSERT INTO Purchases (ClientID, ProductID, Quantity, TotalPrice, PurchaseDate)
VALUES (1, 1, 2, 2.64, '2024-11-15');
