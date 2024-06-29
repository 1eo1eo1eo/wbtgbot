CREATE DATABASE IF NOT EXISTS parserfirst;
CREATE DATABASE IF NOT EXISTS parsersecond;
CREATE DATABASE IF NOT EXISTS parserthird;
CREATE DATABASE IF NOT EXISTS parserfourth;
CREATE DATABASE IF NOT EXISTS parserfifth;
CREATE DATABASE IF NOT EXISTS parsersixth;
CREATE DATABASE IF NOT EXISTS parserseventh;
CREATE DATABASE IF NOT EXISTS parsereighth;
CREATE DATABASE IF NOT EXISTS parsernineth;
CREATE DATABASE IF NOT EXISTS parsertenth;

CREATE USER 'wbbot'@'%' IDENTIFIED BY 'Wbbot12345!';
GRANT ALL PRIVILEGES ON parserfirst.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parsersecond.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parserthird.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parserfourth.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parserfifth.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parsersixth.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parserseventh.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parsereighth.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parsernineth.* TO 'wbbot'@'%';
GRANT ALL PRIVILEGES ON parsertenth.* TO 'wbbot'@'%';
FLUSH PRIVILEGES;

-- Создание таблицы parsers_status для базы данных parserfirst
USE parserfirst;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (1, 'Отключен', 'Женщинам/Платье и сарафаны/Платье');

-- Создание таблицы parsers_status для базы данных parsersecond
USE parsersecond;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (2, 'Отключен', 'Женщинам/Платье и сарафаны/Сарафаны');

-- Создание таблицы parsers_status для базы данных parserthird
USE parserthird;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (3, 'Отключен', 'Женщинам/Верхняя одежда/Косухи');

-- Создание таблицы parsers_status для базы данных parserfourth
USE parserfourth;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (4, 'Отключен', 'Женщинам/Юбки');

-- Создание таблицы parsers_status для базы данных parserfifth
USE parserfifth;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (5, 'Отключен', 'Женщинам/Шорты/Шорты');

USE parsersixth;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (6, 'Отключен', 'Женщины/Джинсы/Джинсы');

USE parserseventh;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (7, 'Отключен', 'Женщины/Брюки/Брюки');

USE parsereighth;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (8, 'Отключен', 'Женщины/Брюки/Леггинсы');

USE parsernineth;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (9, 'Отключен', 'Женщины/Блузки и рубашки/Рубашки');

USE parsertenth;
CREATE TABLE IF NOT EXISTS parsers_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parser_number INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL
);
INSERT INTO parsers_status (parser_number, status, category)
VALUES (10, 'Отключен', 'Женщины/Пиджаки, жилеты и жакеты/Пиджаки');