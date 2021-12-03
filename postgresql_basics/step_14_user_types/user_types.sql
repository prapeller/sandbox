--  domain

DROP DOMAIN IF EXISTS text_no_space_null;
CREATE DOMAIN text_no_space_null AS TEXT NOT NULL CHECK (value ~ '^(?!\s*$).+');

DROP TABLE IF EXISTS agent;
CREATE TABLE agent
(
    first_name text_no_space_null,
    last_name  text_no_space_null
);

INSERT INTO agent
VALUES ('bob', 'taylor');
INSERT INTO agent
VALUES ('', 'taylor');
INSERT INTO agent
VALUES ('   ', 'taylor');
INSERT INTO agent
VALUES (NULL, 'taylor');
INSERT INTO agent
VALUES ('bob taylor maylor', 'taylor');


SELECT *
FROM agent;


ALTER DOMAIN text_no_space_null ADD CONSTRAINT text_no_space_null_length32 CHECK (LENGTH(value) <= 32) NOT VALID;
ALTER DOMAIN text_no_space_null VALIDATE CONSTRAINT text_no_space_null_length32;
DELETE
FROM agent
WHERE LENGTH(first_name) > 32;

INSERT INTO agent
VALUES ('bob taylor maylorsd;falsdkfa;lsdjf;asdkfjasdf', 'taylor');


-- out (2 values (first true 1 row))
CREATE OR REPLACE FUNCTION get_price_boundaries(OUT max_price REAL, OUT min_price REAL) AS
$$
SELECT MAX(unit_price), MIN(unit_price)
FROM products
$$
    LANGUAGE sql;

SELECT get_price_boundaries();
SELECT *
FROM get_price_boundaries();


-- composite type
CREATE TYPE price_bounds AS
(
    max_price REAL,
    min_price REAL
);

DROP FUNCTION IF EXISTS get_price_boundaries;
CREATE OR REPLACE FUNCTION get_price_boundaries() RETURNS SETOF price_bounds AS
$$
SELECT MAX(unit_price), MIN(unit_price)
FROM products
$$
    LANGUAGE sql;

SELECT get_price_boundaries();
SELECT *
FROM get_price_boundaries();


--
CREATE TYPE complex AS
(
    r float8,
    i float8
);

CREATE TABLE math_calcs
(
    math_id SERIAL,
    val     complex
);

INSERT INTO math_calcs(val)
VALUES (ROW (3.0, 4.0)),
       (ROW (2.0, 1.0));

SELECT *
FROM math_calcs;

SELECT (val).r, (val).i
FROM math_calcs;

SELECT (math_calcs.val).r, (math_calcs.val).i
FROM math_calcs;

SELECT math_calcs.val, (math_calcs.val).r, (math_calcs.val).i
FROM math_calcs;

SELECT (math_calcs.val).*
FROM math_calcs;

UPDATE math_calcs
SET val = ROW (5.0, 4.0)
WHERE math_id = 1.0;

SELECT (math_calcs.val).*
FROM math_calcs;

UPDATE math_calcs
SET val.r = 1.0
WHERE math_calcs.math_id = 2;

SELECT (math_calcs.val).*
FROM math_calcs;


-- enumerations

CREATE TABLE chess_title
(
    title_id SERIAL PRIMARY KEY,
    title    TEXT
);

CREATE TABLE chess_player
(
    player_id  SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name  TEXT,
    title_id   INT REFERENCES chess_title (title_id)
);

INSERT INTO chess_title(title)
VALUES ('candidate master'),
       ('fide master'),
       ('international master'),
       ('grand master');

SELECT *
FROM chess_title;

INSERT INTO chess_player (first_name, last_name, title_id)
VALUES ('first1', 'last1', 1),
       ('first2', 'last2', 2),
       ('first3', 'last3', 3),
       ('first4', 'last4', 4);

SELECT player_id, first_name, last_name, title
FROM chess_player cp
         JOIN chess_title ct ON cp.title_id = ct.title_id;

DROP TABLE IF EXISTS chess_player;
DROP TABLE IF EXISTS chess_title;

CREATE TYPE chess_title AS ENUM
    ('candidate master', 'fide master', 'international master');

SELECT ENUM_RANGE(NULL::chess_title);

ALTER TYPE chess_title ADD VALUE 'grand master'
    AFTER
--     BEFORE
    'international master';

CREATE TABLE chess_player
(
    player_id  SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name  TEXT,
    title      chess_title
);

INSERT INTO chess_player (first_name, last_name, title)
VALUES ('first1', 'last1', 'grand master'),
       ('first2', 'last2', 'candidate master'),
       ('first3', 'last3', 'international master'),
       ('first4', 'last4', 'fide master');

-- INSERT INTO chess_player (first_name, last_name, title)
-- VALUES ('first1', 'last1', 'labuda');


-- homework
-- 1. Переписать функцию, которую мы разработали ранее в одном из ДЗ таким образом, чтобы функция возвращала экземпляр композитного типа. Вот та самая функция:

-- create or replace function get_salary_boundaries_by_city(
-- 	emp_city varchar, out min_salary numeric, out max_salary numeric)
-- AS
-- $$
-- 	SELECT MIN(salary) AS min_salary,
-- 	   	   MAX(salary) AS max_salary
--   	FROM employees
-- 	WHERE city = emp_city
-- $$ language sql;

CREATE TYPE price_bounds_by_city AS
(
    min_price NUMERIC,
    max_price NUMERIC
);

CREATE OR REPLACE FUNCTION get_salary_boundaries_by_city(
    emp_city VARCHAR) RETURNS SETOF price_bounds_by_city
AS
$$
SELECT MIN(salary) AS min_salary,
       MAX(salary) AS max_salary
FROM employees
WHERE city = emp_city
$$ LANGUAGE sql;

SELECT *
FROM get_salary_boundaries_by_city('London');


-- 2. Задание состоит из пунктов:
-- Создать перечисление армейских званий США, включающее следующие значения: Private, Corporal, Sergeant
-- Вывести все значения из перечисления.
-- Добавить значение Major после Sergeant в перечисление
-- Создать таблицу личного состава с колонками: person_id, first_name, last_name, person_rank (типа перечисления)
-- Добавить несколько записей, вывести все записи из таблицы

CREATE TYPE army_rank AS ENUM
    ('Private', 'Corporal', 'Sergeant');

SELECT ENUM_RANGE(NULL::army_rank);
ALTER TYPE army_rank ADD VALUE 'Major'
    AFTER
--     BEFORE
    'Sergeant';

DROP TABLE IF EXISTS personnel;
CREATE TABLE personnel
(
    person_id   SERIAL PRIMARY KEY,
    first_name  VARCHAR,
    last_name   VARCHAR,
    person_rank army_rank
);

INSERT INTO personnel (first_name, last_name, person_rank) VALUES
('bob', 'marley', 'Private'),
('bob', 'marley', 'Corporal'),
('bob', 'marley', 'Sergeant'),
('bob', 'marley', 'Major');

SELECT * from personnel;