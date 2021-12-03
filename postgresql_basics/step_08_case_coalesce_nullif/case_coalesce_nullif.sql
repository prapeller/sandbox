-- case when

SELECT product_name,
       unit_price,
       units_in_stock,
       CASE
           WHEN units_in_stock >= 100 THEN 'lots'
           WHEN units_in_stock >= 50 AND units_in_stock < 100 THEN 'average'
           WHEN units_in_stock >= 1 AND units_in_stock < 50 THEN 'low'
           ELSE 'absent'
           END AS amount
FROM products
ORDER BY units_in_stock;


SELECT order_id,
       order_date,
       CASE
           WHEN DATE_PART('month', order_date) BETWEEN 3 AND 5 THEN 'spring'
           WHEN DATE_PART('month', order_date) BETWEEN 6 AND 8 THEN 'summer'
           WHEN DATE_PART('month', order_date) BETWEEN 9 AND 11 THEN 'autumn'
           ELSE 'winter'
           END AS season
FROM orders
ORDER BY order_date;


SELECT product_name,
       unit_price,
       CASE
           WHEN unit_price >= 30 THEN 'expensive'
           WHEN unit_price < 30 THEN 'not expensive'
           ELSE 'unknown'
           END AS price_desc
FROM products
ORDER BY unit_price;


-- coalesce, nullif

SELECT *
FROM orders
LIMIT 10;


SELECT order_id, order_date, COALESCE(ship_region, 'unknown') AS ship_region
FROM orders
LIMIT 10;

SELECT *
FROM employees;

SELECT first_name, last_name, COALESCE(region, 'unknown') AS region
FROM employees;

SELECT *
FROM customers;

SELECT contact_name, COALESCE(NULLIF(city, 'Århus'), 'WHAAAAAAAAT!?!??!?!?!!??!?!?!??!?!??!?!?!?') AS city
FROM customers;

SELECT *
FROM orders
WHERE order_id > 11010;

SELECT order_id,
       required_date,
       COALESCE(TO_CHAR(NULLIF(shipped_date, required_date), 'FMYYYY-MM-DD'), 'the same day!') AS shipped_on
FROM orders
WHERE shipped_date IS NOT NULL
  AND shipped_date = required_date;

-- homework

-- insert into customers(customer_id, contact_name, city, country, company_name)
-- values
-- ('AAAAA', 'Alfred Mann', NULL, 'USA', 'fake_company'),
-- ('BBBBB', 'Alfred Mann', NULL, 'Austria','fake_company');

-- 1. Вывести имя контакта заказчика, его город и страну, отсортировав по возрастанию по имени контакта и городу,
-- а если город равен NULL, то по имени контакта и стране. Проверить результат, используя заранее вставленные строки.

SELECT contact_name, city, country
FROM customers
ORDER BY contact_name,
         (
             CASE
                 WHEN city IS NULL THEN country
                 ELSE city
                 END
             );

-- 2. Вывести наименование продукта, цену продукта и столбец со значениями
-- too expensive если цена >= 100
-- average если цена >=50 но < 100
-- low price если цена < 50
SELECT product_name,
       unit_price,
       CASE
           WHEN unit_price >= 100 THEN 'expensive'
           WHEN unit_price >= 50 AND unit_price < 100 THEN 'average'
           ELSE 'low price' END AS price_description
FROM products
ORDER BY unit_price;

-- 3. Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и значение 'no orders' если order_id = NULL.
SELECT contact_name, COALESCE(o.order_id::TEXT, 'no orders') AS ord
FROM customers c
         LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- 4. Вывести ФИО сотрудников и их должности. В случае если должность = Sales Representative вывести вместо неё Sales Stuff.
SELECT (first_name || ' ' || last_name) as name,
       CASE
           WHEN title = 'Sales Representative' THEN 'Sales Stuff'
           ELSE title
           END AS title
FROM employees;