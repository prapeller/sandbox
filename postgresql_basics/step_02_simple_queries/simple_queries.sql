-- create database northwind;

SELECT *
FROM products;

SELECT product_id, product_name, unit_price
FROM products;

SELECT product_id, product_name, (unit_price * products.units_in_stock) AS overs
FROM products;

-- distinct

SELECT *
FROM employees;

SELECT DISTINCT city
FROM employees;

SELECT DISTINCT country
FROM employees;

SELECT DISTINCT city, country
FROM employees;

-- count

SELECT *
FROM orders;

SELECT COUNT(*)
FROM orders;

SELECT *
FROM employees;

SELECT COUNT(country)
FROM employees;

SELECT COUNT(DISTINCT country)
FROM employees;

-- hw
-- 1. Выбрать все данные из таблицы customers
SELECT *
FROM customers;

--
-- 2. Выбрать все записи из таблицы customers, но только колонки "имя контакта" и "город"
SELECT contact_name, city
FROM customers;

--
-- 3. Выбрать все записи из таблицы orders, но взять две колонки: идентификатор заказа и колонку, значение в которой мы рассчитываем как разницу между датой отгрузки и датой формирования заказа.
--
SELECT order_id, (shipped_date - orders.order_date)
FROM orders;

-- 4. Выбрать все уникальные города в которых "зарегистрированы" заказчики
--
SELECT DISTINCT city
FROM customers;

-- 5. Выбрать все уникальные сочетания городов и стран в которых "зарегистрированы" заказчики
--
SELECT DISTINCT city, country
FROM customers;

-- 6. Посчитать кол-во заказчиков
--
SELECT COUNT(customer_id)
FROM customers;

-- 7. Посчитать кол-во уникальных стран в которых "зарегистрированы" заказчики
SELECT DISTINCT country
FROM customers;

-- where

SELECT company_name, contact_name, phone, country
FROM customers
WHERE country = 'USA';

SELECT *
FROM products
WHERE unit_price > 20;
SELECT COUNT(*)
FROM products
WHERE unit_price > 20;

SELECT *
FROM products
WHERE discontinued = 1;

SELECT *
FROM customers
WHERE city != 'Berlin';

SELECT *
FROM orders
WHERE order_date > '1998-03-01';

-- and / or

SELECT *
FROM products
WHERE unit_price > 25
  AND unit_price < 40
  AND units_in_stock > 40;

SELECT *
FROM customers
WHERE city = 'Berlin'
   OR city = 'London'
   OR city = 'San Francisco';

SELECT *
FROM orders
WHERE NOT (shipped_date < '1998-04-30' AND freight > 75)
   OR (shipped_date >= '1998-04-30' AND freight < 75);

-- between

SELECT *
FROM orders
WHERE freight >= 20
  AND freight <= 40;

-- the same with between including boundaries
SELECT *
FROM orders
WHERE freight BETWEEN 20 AND 40;

SELECT *
FROM orders
WHERE order_date BETWEEN '1998-03-30' AND '1998-04-30';

-- in and not in

SELECT *
FROM customers
WHERE country = 'Mexico'
   OR country = 'Germany'
   OR country = 'USA';

SELECT *
FROM customers
WHERE country IN ('Mexico', 'Germany', 'USA');

SELECT *
FROM products
WHERE category_id IN (1, 3, 5);

SELECT *
FROM products
WHERE category_id NOT IN (1, 3, 5);

-- order by

SELECT DISTINCT country
FROM customers
ORDER BY country; -- implicit 'asc'

SELECT DISTINCT country
FROM customers
ORDER BY country DESC; -- explicit 'desc'

SELECT DISTINCT country, city
FROM customers
ORDER BY country DESC, city ASC;

-- min, max, avg, sum

SELECT ship_city, order_date
FROM orders
WHERE ship_city = 'London'
ORDER BY order_date;

SELECT MIN(order_date)
FROM orders
WHERE ship_city = 'London';

SELECT ship_city, order_date
FROM orders
WHERE ship_city = 'London'
ORDER BY order_date DESC;

SELECT MAX(order_date)
FROM orders
WHERE ship_city = 'London';

SELECT AVG(unit_price)
FROM products
WHERE discontinued != 1;

SELECT SUM(units_in_stock) AS total_units_in_stock
FROM products
WHERE discontinued != 1;

-- homework

-- 1. Выбрать все заказы из стран France, Austria, Spain
--
SELECT *
FROM orders
WHERE ship_country IN ('France', 'Austria', 'Spain');

-- 2. Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
--
SELECT *
FROM orders
ORDER BY required_date DESC, shipped_date;

-- 3. Выбрать минимальную цену товара среди тех продуктов, которых в продаже более 30 единиц.
--
SELECT MIN(unit_price) AS min_unit_price
FROM products
WHERE units_in_stock > 30;

-- 4. Выбрать максимальное кол-во единиц товара среди тех продуктов, цена которых более 30 у.е.
--
SELECT MAX(units_in_stock)
FROM products
WHERE units_in_stock > 30;

-- 5. Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
--
SELECT AVG(shipped_date - order_date)
FROM orders
WHERE ship_country = 'USA';

-- 6. Найти сумму, на которую имеется товаров (кол-во * цену) причём таких, которые планируется продавать и в будущем (см. на поле discontinued)
SELECT SUM(unit_price * units_in_stock)
FROM products
WHERE discontinued <> 1;

-- like

SELECT last_name, first_name
FROM employees
WHERE first_name LIKE '%n';

SELECT last_name, first_name
FROM employees
WHERE last_name LIKE 'B%';

SELECT last_name, first_name
FROM employees
WHERE last_name LIKE '__ch%';

-- limit

SELECT product_name, unit_price
FROM products
WHERE discontinued <> 1
ORDER BY unit_price DESC
LIMIT 10;

-- NULL

SELECT ship_city, ship_region, ship_country
FROM orders
WHERE ship_region IS NULL;


SELECT ship_city, ship_region, ship_country
FROM orders
WHERE ship_region IS NOT NULL;

-- group by

SELECT ship_country, COUNT(*) AS qty
FROM orders
WHERE freight > 50
GROUP BY ship_country
ORDER BY qty DESC;

SELECT category_id, SUM(units_in_stock) AS stock_qty
FROM products
GROUP BY category_id
ORDER BY stock_qty DESC
LIMIT 5;

-- having

SELECT category_id, SUM(unit_price * units_in_stock)
FROM products
WHERE discontinued <> 1
GROUP BY category_id
HAVING SUM(unit_price * units_in_stock) > 10000
ORDER BY category_id DESC
LIMIT 2;

-- union, intersect, except

SELECT country
FROM customers
UNION
SELECT country
FROM employees;

SELECT country
FROM customers
UNION ALL
SELECT country
FROM employees;

SELECT country
FROM customers
INTERSECT
SELECT country
FROM suppliers;

SELECT country
FROM customers
    EXCEPT
SELECT country
FROM suppliers;

SELECT country
FROM customers
    EXCEPT ALL
SELECT country
FROM suppliers;

-- hw
-- 1. Выбрать все записи заказов в которых наименование страны отгрузки начинается с 'U'
--
SELECT *
FROM orders
WHERE ship_country LIKE 'U%';

-- 2. Выбрать записи заказов (включить колонки идентификатора заказа, идентификатора заказчика, веса и страны отгрузки), которые должны быть отгружены в страны имя которых начинается с 'N', отсортировать по весу (по убыванию) и вывести только первые 10 записей.
--
SELECT order_id, customer_id, freight, ship_country
FROM orders
WHERE ship_country LIKE 'N%'
ORDER BY freight DESC
LIMIT 10;

-- 3. Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен
--
SELECT first_name, last_name, home_phone, region
FROM employees
WHERE region IS NULL;

-- 4. Подсчитать кол-во заказчиков регион которых известен
--
SELECT COUNT(customer_id)
FROM customers
WHERE region IS NOT NULL;

-- 5. Подсчитать кол-во поставщиков в каждой из стран и отсортировать результаты группировки по убыванию кол-ва
--
SELECT country, COUNT(supplier_id) AS supplier_qty
FROM suppliers
GROUP BY country
ORDER BY supplier_qty DESC;

-- 6. Подсчитать суммарный вес заказов (в которых известен регион) по странам, затем отфильтровать по суммарному весу (вывести только те записи где суммарный вес больше 2750) и отсортировать по убыванию суммарного веса.
--
SELECT ship_country, SUM(freight) AS sum_freight
FROM orders
WHERE ship_region IS NOT NULL
GROUP BY ship_country
HAVING SUM(freight) > 2750
ORDER BY sum_freight DESC;

-- 7. Выбрать все уникальные страны заказчиков и поставщиков и отсортировать страны по возрастанию
--
SELECT country
FROM customers
UNION
SELECT country
FROM suppliers
ORDER BY country;

-- 8. Выбрать такие страны в которых "зарегистрированы" одновременно и заказчики и поставщики и работники.
--
SELECT country
FROM suppliers
INTERSECT
SELECT country
FROM customers
INTERSECT
SELECT country
FROM employees;

-- 9. Выбрать такие страны в которых "зарегистрированы" одновременно заказчики и поставщики, но при этом в них не "зарегистрированы" работники.
SELECT country
FROM customers
INTERSECT
SELECT country
FROM suppliers
    EXCEPT
SELECT country
FROM employees;