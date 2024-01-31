-- Active: 1706528682669@@127.0.0.1@3306@store
CREATE DATABASE store;
USE store;
CREATE TABLE product(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description TEXT,
    price INT,
    quantity INT,
    id_category INT
);
CREATE TABLE category(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);

INSERT INTO category (name) VALUES
('Électronique'),
('Vêtements'),
('Maison'),
('Alimentation'),
('Sport');

INSERT INTO product (name, description, price, quantity, id_category) VALUES
('Téléviseur OLED 4K', 'Écran 55 pouces', 799.99, 10, 1),
('Chemise en coton', 'Taille M, couleur bleue', 29.99, 50, 2),
('Aspirateur sans sac', 'Puissance 1200W', 129.99, 20, 3),
('Pâtes alimentaires', 'Spaghetti, paquet de 500g', 1.99, 100², 4),
('Raquette de tennis', 'Marque Pro-X', 59.99, 15, 5);