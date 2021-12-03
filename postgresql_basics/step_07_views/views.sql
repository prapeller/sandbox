-- creating views

CREATE VIEW products_suppliers_categories AS
SELECT product_name,
       quantity_per_unit,
       unit_price,
       units_in_stock,
       company_name,
       contact_name,
       phone,
       category_name,
       description
FROM products p
         JOIN suppliers s ON p.supplier_id = s.supplier_id
         JOIN categories c ON p.category_id = c.category_id;

SELECT *
FROM products_suppliers_categories;


SELECT *
FROM products_suppliers_categories
WHERE unit_price > 10;

DROP VIEW IF EXISTS products_suppliers_categories;

SELECT *
FROM orders;

CREATE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 50;

SELECT *
FROM heavy_orders
ORDER BY freight;

-- replace

CREATE OR REPLACE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 100;

CREATE VIEW products_suppliers_categories AS
SELECT product_name,
       quantity_per_unit,
       unit_price,
       units_in_stock,
       company_name,
       contact_name,
       phone
FROM products p
         JOIN suppliers s ON p.supplier_id = s.supplier_id
         JOIN categories c ON p.category_id = c.category_id;

CREATE OR REPLACE VIEW products_suppliers_categories AS
SELECT product_name,
--        discontinued
       quantity_per_unit,
       unit_price,
       units_in_stock,
       company_name,
       contact_name,
       phone
FROM products p
         JOIN suppliers s ON p.supplier_id = s.supplier_id
         JOIN categories c ON p.category_id = c.category_id;

-- SELECT *
-- FROM products_suppliers_categories
-- WHERE discontinued = 1;

-- rename

ALTER VIEW products_suppliers_categories RENAME TO psc_old;

CREATE OR REPLACE VIEW products_suppliers_categories AS
SELECT product_name,
       discontinued,
       quantity_per_unit,
       unit_price,
       units_in_stock,
       company_name,
       contact_name,
       phone,
       category_name,
       description
FROM products p
         JOIN suppliers s ON p.supplier_id = s.supplier_id
         JOIN categories c ON p.category_id = c.category_id;

SELECT *
FROM products_suppliers_categories
WHERE discontinued = 1;


SELECT MAX(order_id)
FROM orders;

-- insert

INSERT INTO heavy_orders
VALUES (11078, 'ERNSH', 3, '1998-02-18', '1998-03-18', '1998-02-23', 1, 162.75, 'Ernst Handel', 'Kirchgasse 6', 'Graz',
        NULL, 8010, 'Austria');

SELECT *
FROM heavy_orders
ORDER BY order_id DESC;

SELECT MIN(freight)
FROM orders;

-- delete where

DELETE
FROM heavy_orders
WHERE freight < 0.05; -- delete 0

SELECT MIN(freight)
FROM orders;

SELECT MIN(freight)
FROM heavy_orders;

DELETE
FROM order_details
WHERE order_id = 10854;

DELETE
FROM heavy_orders
WHERE freight < 100.25;

SELECT MIN(freight)
FROM heavy_orders;

-- insert where

SELECT *
FROM heavy_orders
ORDER BY freight;

INSERT INTO heavy_orders
VALUES (11901, 'QUEEN', 7, '1997-09-05', '1997-10-03', '1997-09-10', 2, 5.81, 'Queen Cozinha',
        'Alameda dos Canàrios, 891', 'Sao Paulo', 'SP', '05487-020', 'Brazil');

SELECT *
FROM heavy_orders
WHERE order_id = 11901;
-- can insert through view, but not added to view

CREATE OR REPLACE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 100
WITH CASCADED CHECK OPTION;

INSERT INTO heavy_orders
VALUES (11902, 'QUEEN', 7, '1997-09-05', '1997-10-03', '1997-09-10', 2, 5.81, 'Queen Cozinha',
        'Alameda dos Canàrios, 891', 'Sao Paulo', 'SP', '05487-020', 'Brazil');
-- cant insert through view not consisting about 'cascaded check option'


-- homework

-- 1. Создать представление, которое выводит следующие колонки:
-- order_date, required_date, shipped_date, ship_postal_code, company_name, contact_name, phone, last_name, first_name, title из таблиц orders, customers и employees.

CREATE VIEW orders_customers_employees AS
SELECT order_date,
       required_date,
       shipped_date,
       ship_postal_code,
       company_name,
       contact_name,
       phone,
       last_name,
       first_name,
       title
FROM orders o
         JOIN customers c ON o.customer_id = c.customer_id
         JOIN employees e ON o.employee_id = e.employee_id;
-- Сделать select к созданному представлению, выведя все записи, где order_date больше 1го января 1997 года.

SELECT *
FROM orders_customers_employees
WHERE order_date > '1997-01-01';

-- 2. Создать представление, которое выводит следующие колонки:
-- order_date, required_date, shipped_date, ship_postal_code, ship_country, company_name, contact_name, phone,
-- last_name, first_name, title из таблиц orders, customers, employees.

ALTER VIEW orders_customers_employees RENAME TO oce_old;

CREATE VIEW orders_customers_employees AS
SELECT order_date,
       required_date,
       shipped_date,
       ship_postal_code,
       ship_country,
       company_name,
       contact_name,
       phone,
       last_name,
       first_name,
       title
FROM orders o
         JOIN customers c ON o.customer_id = c.customer_id
         JOIN employees e ON o.employee_id = e.employee_id;

-- Попробовать добавить к представлению (после его создания) колонки ship_country, postal_code и reports_to (добавить не
-- в конец, а куда-нибудь посерединке). Убедиться, что проихсодит ошибка. Переименовать представление и создать новое уже с дополнительными колонками.
--
-- Сделать к нему запрос, выбрав все записи, отсортировав их по ship_country.
--
SELECT *
FROM orders_customers_employees
ORDER BY ship_country DESC;

-- Удалить переименованное представление.
--
DROP VIEW oce_old;

-- 3.  Создать представление "активных" (discontinued = 0) продуктов, содержащее все колонки. Представление должно быть
-- защищено от вставки записей, в которых discontinued = 1.
--
CREATE VIEW active_products AS
SELECT *
FROM products
WHERE discontinued = 0
WITH CASCADED CHECK OPTION;

SELECT *
FROM products;

-- Попробовать сделать вставку записи с полем discontinued = 1 - убедиться, что не проходит.
INSERT INTO active_products VALUES
(80,'prod',1,1,1,1,1,1,1,0);

-- INSERT INTO active_products VALUES
-- (81,'prod',1,1,1,1,1,1,1,1);