CREATE TABLE student
(
    student_id SERIAL,
    first_name VARCHAR(10),
    last_name  VARCHAR(10),
    birthday   DATE,
    phone      VARCHAR(10)
);

CREATE TABLE cathedra
(
    cathedra_id   SERIAL,
    cathedra_name VARCHAR(10),
    dean          VARCHAR(10)
);

ALTER TABLE student
    ADD COLUMN middle_name VARCHAR;

ALTER TABLE student
    ADD COLUMN rating FLOAT;

ALTER TABLE student
    ADD COLUMN enrolled DATE;

ALTER TABLE cathedra
    RENAME TO chair;

ALTER TABLE chair
    RENAME cathedra_id TO chair_id;

ALTER TABLE chair
    RENAME cathedra_name TO chair_name;

ALTER TABLE student
    ALTER COLUMN first_name SET DATA TYPE VARCHAR(55);
ALTER TABLE student
    ALTER COLUMN first_name SET DATA TYPE VARCHAR(55);
ALTER TABLE student
    ALTER COLUMN phone SET DATA TYPE INTEGER USING phone::INTEGER;

-- primary key

CREATE TABLE faculty
(
    faculty_id   SERIAL, -- PRIMARY KEY,
    faculty_name VARCHAR(50),

    CONSTRAINT pk_fac_id PRIMARY KEY (faculty_id)
);

INSERT INTO faculty (faculty_name)
VALUES ('fac1'),
       ('fac2'),
       ('fac3');

TRUNCATE TABLE faculty; -- implicit CONTINUE IDENTITY
TRUNCATE TABLE faculty RESTART IDENTITY;

DROP TABLE IF EXISTS faculty;

SELECT *
FROM faculty;

SELECT constraint_name
FROM information_schema.key_column_usage
WHERE table_name = 'faculty'
  AND table_schema = 'public'
  AND column_name = 'faculty_id';

ALTER TABLE faculty
    DROP CONSTRAINT pk_fac_id;

-- foreign key (testdb)


DROP TABLE IF EXISTS publisher;
CREATE TABLE publisher
(
    id      SERIAL,
    name    VARCHAR(128) NOT NULL,
    address TEXT,

    CONSTRAINT pk_publisher_id PRIMARY KEY (id)
);

DROP TABLE IF EXISTS book;
CREATE TABLE book
(
    id           SERIAL,
    title        TEXT        NOT NULL,
    isbn         VARCHAR(32) NOT NULL,
    publisher_id INT,
    CONSTRAINT pk_book_id PRIMARY KEY (id),
    CONSTRAINT fk_book_publisher_id FOREIGN KEY (publisher_id) REFERENCES publisher (id)
);

INSERT INTO publisher (name, address)
VALUES ('publisher1', 'add1'),
       ('publisher2', 'add2'),
       ('publisher3', 'add3'),
       ('publisher4', 'add4');

INSERT INTO book (title, isbn, publisher_id)
VALUES ('title1', 'isbn1', 1),
       ('title2', 'isbn2', 2),
       ('title3', 'isbn3', 3),
       ('title4', 'isbn4', 4);

INSERT INTO book (title, isbn, publisher_id)
VALUES ('title5', 'isbn5', 4);
-- INSERT INTO book (title, isbn, publisher_id)
-- VALUES ('title5', 'isbn5', 10);

ALTER TABLE book
    DROP CONSTRAINT fk_book_publisher_id;

INSERT INTO book (title, isbn, publisher_id)
VALUES ('title5', 'isbn5', 10);

-- check

DROP TABLE IF EXISTS book;
CREATE TABLE book
(
    id           SERIAL,
    title        TEXT        NOT NULL,
    isbn         VARCHAR(32) NOT NULL,
    publisher_id INT,
    CONSTRAINT pk_book_id PRIMARY KEY (id),
    CONSTRAINT fk_book_publisher_id FOREIGN KEY (publisher_id) REFERENCES publisher (id)
);

SELECT *
FROM book;

ALTER TABLE book
    ADD COLUMN price DECIMAL
        CONSTRAINT CHK_book_price CHECK ( price >= 0 );

INSERT INTO book (title, isbn, publisher_id, price)
VALUES ('title1', 'isbn1', 1, 10),
       ('title2', 'isbn2', 2, 100);

-- INSERT INTO book (title, isbn, publisher_id, price) VALUES
-- ('title3', 'isbn3', 3, -1);


-- default

CREATE TABLE customer
(
    id     SERIAL,
    name   TEXT,
    status CHAR DEFAULT 'r',

    CONSTRAINT pk_customer_id PRIMARY KEY (id),
    CONSTRAINT chk_customer_status CHECK ( status = 'r' OR status = 'p' )
);

INSERT INTO customer (name)
VALUES ('name');

ALTER TABLE customer
    ALTER COLUMN status SET DEFAULT 'p';

INSERT INTO customer (name)
VALUES ('name2');

-- sequenses

CREATE SEQUENCE seq_1;

SELECT NEXTVAL('seq_1');
SELECT CURRVAL('seq_1');
SELECT LASTVAL();

SELECT SETVAL('seq_1', 3, TRUE);
SELECT CURRVAL('seq_1');
SELECT NEXTVAL('seq_1');

SELECT SETVAL('seq_1', 3, FALSE);
SELECT CURRVAL('seq_1');
SELECT NEXTVAL('seq_1');

CREATE SEQUENCE IF NOT EXISTS seq_2 INCREMENT 16;
SELECT NEXTVAL('seq_2');

CREATE SEQUENCE IF NOT EXISTS seq_3
    INCREMENT 16
    MINVALUE 0
    MAXVALUE 128
    START WITH 0;
SELECT NEXTVAL('seq_3');
ALTER SEQUENCE seq_3 RENAME TO seq_4;
ALTER SEQUENCE seq_4 RESTART WITH 16;

SELECT NEXTVAL('seq_4');
DROP SEQUENCE seq_4;

-- sequences and tables

DROP TABLE IF EXISTS book;

CREATE TABLE IF NOT EXISTS book
(
    id           SERIAL      NOT NULL,
    title        TEXT        NOT NULL,
    isbn         VARCHAR(32) NOT NULL,
    publisher_id INTEGER     NOT NULL,

    CONSTRAINT PK_book_id PRIMARY KEY (id)
);

SELECT *
FROM book;

CREATE SEQUENCE IF NOT EXISTS book_id_seq
    START WITH 1 OWNED BY book.id;

ALTER TABLE book
    ALTER COLUMN id SET DEFAULT NEXTVAL('book_id_seq');

INSERT INTO book (title, isbn, publisher_id)
VALUES ('title1', 'isbn1', 1);


DROP TABLE IF EXISTS book;
CREATE TABLE IF NOT EXISTS book
(
    id           INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    title        TEXT                             NOT NULL,
    isbn         VARCHAR(32)                      NOT NULL,
    publisher_id INTEGER                          NOT NULL,

    CONSTRAINT PK_book_id PRIMARY KEY (id)
);

INSERT INTO book (title, isbn, publisher_id)
VALUES ('title1', 'isbn1', 1),
       ('title1', 'isbn1', 1);

INSERT INTO book
-- OVERRIDING SYSTEM VALUE
VALUES (3, 'title1', 'isbn1', 1);

DROP TABLE IF EXISTS book;
CREATE TABLE IF NOT EXISTS book
(
    id           INT GENERATED ALWAYS AS IDENTITY (START WITH 10 INCREMENT BY 5) NOT NULL,
    title        TEXT                                                            NOT NULL,
    isbn         VARCHAR(32)                                                     NOT NULL,
    publisher_id INTEGER                                                         NOT NULL,

    CONSTRAINT PK_book_id PRIMARY KEY (id)
);

INSERT INTO book (title, isbn, publisher_id)
VALUES ('title1', 'isbn1', 1),
       ('title1', 'isbn1', 1);

-- insert

INSERT INTO author
VALUES (5, 'name5');

SELECT *
FROM author;

INSERT INTO author (name)
VALUES ('name6');

SELECT *
FROM author;

INSERT INTO author (name)
VALUES ('name7'),
       ('name8'),
       ('name9'),
       ('name10');
;

SELECT *
FROM author;

-- select * into
SELECT *
INTO best_authors
FROM author
WHERE id < 6;

SELECT *
FROM best_authors;

-- insert into ... select
INSERT INTO best_authors
SELECT *
FROM author
WHERE id BETWEEN 6 AND 8;

SELECT *
FROM best_authors;

-- update, delete

SELECT *
FROM author;

UPDATE author
SET name = 'NAME5'
WHERE id = 5;

DELETE
FROM author
WHERE id = 10;

SELECT *
FROM author;

DELETE
FROM author;

TRUNCATE TABLE author RESTART IDENTITY;

SELECT *
FROM author;

-- returning

INSERT INTO author (name)
VALUES ('name10')
RETURNING *;

INSERT INTO author (name)
VALUES ('name11')
RETURNING name;

UPDATE author
SET name = 'NAME11'
WHERE id = 2
RETURNING *;

-- homework
-- ДЗ 2 по DDL
-- 1. Создать таблицу exam с полями:
--
-- - идентификатора экзамена - автоинкрементируемый, уникальный, запрещает NULL;
-- - наименования экзамена
-- - даты экзамена
--

DROP TABLE IF EXISTS exam;

CREATE TABLE exam
(
    id   INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    name VARCHAR(128)                                                       NOT NULL,
    date DATE DEFAULT NOW(),

    CONSTRAINT pk_exam_id PRIMARY KEY (id)
);

-- 2. Удалить ограничение уникальности с поля идентификатора
--

ALTER TABLE exam
    DROP CONSTRAINT pk_exam_id;

-- 3. Добавить ограничение первичного ключа на поле идентификатора
--
ALTER TABLE exam
    ADD CONSTRAINT pk_exam_id PRIMARY KEY (id);

-- 4. Создать таблицу person с полями
--
-- - идентификатора личности (простой int, первичный ключ)
-- - имя
-- - фамилия
--

DROP TABLE IF EXISTS person CASCADE;
CREATE TABLE person
(
    id       INT PRIMARY KEY,
    name     VARCHAR(255),
    lastname VARCHAR(255)
);

-- 5. Создать таблицу паспорта с полями:
--
-- - идентификатора паспорта (простой int, первичный ключ)
-- - серийный номер (простой int, запрещает NULL)
-- - регистрация
-- - ссылка на идентификатор личности (внешний ключ)
--
DROP TABLE IF EXISTS passport;
CREATE TABLE passport
(
    id           INT PRIMARY KEY,
    serial       INT NOT NULL,
    registration VARCHAR(512),
    person_id    INT NOT NULL,

    CONSTRAINT fk_passport_person_id FOREIGN KEY (person_id) REFERENCES person (id)
);

-- 6. Добавить колонку веса в таблицу book (создавали ранее) с ограничением, проверяющим вес (больше 0 но меньше 100)
--
ALTER TABLE book
    ADD COLUMN weight DECIMAL
        CONSTRAINT chk_book_weight CHECK ( weight > 0 AND weight <= 100);

-- 7. Убедиться в том, что ограничение на вес работает (попробуйте вставить невалидное значение)
--
INSERT INTO book (title, isbn, publisher_id, weight)
VALUES ('title1', 'isbn1', 1, 0);

SELECT *
FROM book;

INSERT INTO book (title, isbn, publisher_id, weight)
VALUES ('title1', 'isbn1', 1, 30);

-- 8. Создать таблицу student с полями:
--
-- - идентификатора (автоинкремент)
-- - полное имя
-- - курс (по умолчанию 1)
--
DROP TABLE IF EXISTS student;
CREATE TABLE student
(
    id     INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
    name   VARCHAR(255),
    course INT DEFAULT 1 NOT NULL
);

-- 9. Вставить запись в таблицу студентов и убедиться, что ограничение на вставку значения по умолчанию работает
--
CREATE SEQUENCE IF NOT EXISTS student_name_seq
    START WITH 1;

INSERT INTO student (name)
VALUES (CONCAT('name', NEXTVAL('student_name_seq')));

-- 10. Удалить ограничение "по умолчанию" из таблицы студентов
--
ALTER TABLE student
    ALTER COLUMN course DROP DEFAULT;

INSERT INTO student (name, course)
VALUES (CONCAT('name', NEXTVAL('student_name_seq')), 0);

-- 11. Подключиться к БД northwind и добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
--
SELECT *
FROM products;

ALTER TABLE products
    ADD CONSTRAINT chk_unit_price CHECK ( unit_price > 0);

-- 12. "Навесить" автоинкрементируемый счётчик на поле product_id таблицы products (БД northwind). Счётчик должен
-- начинаться с числа следующего за максимальным значением по этому столбцу.
--

select max(product_id) from products;

CREATE SEQUENCE IF NOT EXISTS product_id_seq START WITH 79 OWNED BY products.product_id;

ALTER TABLE products
    ALTER COLUMN product_id SET DEFAULT nextval('product_id_seq');

-- 13. Произвести вставку в products (не вставляя идентификатор явно) и убедиться, что автоинкремент работает.
-- Вставку сделать так, чтобы в результате команды вернулось значение, сгенерированное в качестве идентификатора.
INSERT INTO products (product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock,
                      units_on_order, reorder_level, discontinued)
VALUES ('prod', 1, 1, 1, 1, 1, 1, 1, 1);

SELECT *
FROM products;