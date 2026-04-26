pip install mysql-connector-python



CREATE DATABASE agenda_db;
USE agenda_db;

CREATE TABLE contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(20),
    cumpleanos VARCHAR(50)
);