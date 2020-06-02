CREATE TABLE Restoran
(
    id numeric(4) NOT NULL PRIMARY KEY,
    name varchar(20) NOT NULL,
    Address varchar(20) NOT NULL,
    City varchar(15) NOT NULL,
    Street varchar(2) NOT NULL,
    Contact varchar(16) NOT NULL,
    Phonenumeric varchar(12) NOT NULL,
--    meny numeric(6) NOT NULL, REFERENCES meny(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Personal
(
    id numeric(6) NOT NULL, PRIMARY KEY,
    f_name varchar(30) NOT NULL,
    l_name  varchar(30) NOT NULL,
    vacancy varchar(30) NOT NULL ,
    restoran_id numeric(3) NOT NULL, REFERENCES restoran(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE country
(
    id numeric(6) NOT NULL, PRIMARY KEY,
    name varchar(30) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE dish
(
    id numeric(6) NOT NULL, PRIMARY KEY,
    name varchar(30) NOT NULL,
    status varchar(30) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE meny
(
    id numeric(6) NOT NULL, PRIMARY KEY,
    name varchar(30) NOT NULL,
    id_dish numeric(6) NOT NULL, REFERENCES dish(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE Restoran
  ADD COLUMN meny numeric(6) REFERENCES meny(id);

CREATE INDEX name ON country(name);
--psql objectrocket -h 127.0.0.1 -d some_database -f -a test.sql
--CREATE DATABASE django_numericro;
--ALTER TABLE Restoran
--ADD COLUMN meny numeric(6) REFERENCES meny(id);