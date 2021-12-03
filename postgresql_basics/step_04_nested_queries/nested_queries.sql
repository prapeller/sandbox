-- nested

SELECT company_name
FROM suppliers
WHERE country IN (SELECT DISTINCT country
                  FROM customers)
ORDER BY company_name;

-- by joins
SELECT DISTINCT s.company_name
FROM suppliers s
         JOIN customers c ON s.country = c.country
ORDER BY s.company_name;

SELECT c.category_name, SUM(units_in_stock) sum
FROM products p
         JOIN categories c ON p.category_id = c.category_id
GROUP BY category_name
ORDER BY sum DESC
LIMIT (SELECT (MIN(product_id) + 4) FROM products);

SELECT AVG(units_in_stock)
FROM products;

SELECT product_name, units_in_stock
FROM products
WHERE units_in_stock > (
    SELECT AVG(units_in_stock)
    FROM products)
ORDER BY units_in_stock;

-- where exists

SELECT company_name, contact_name
FROM customers c
WHERE EXISTS(SELECT o.customer_id
             FROM orders o
             WHERE o.customer_id = c.customer_id
               AND freight BETWEEN 50 AND 100
          );

SELECT company_name, contact_name
FROM customers c
WHERE EXISTS(SELECT o.customer_id
             FROM orders o
             WHERE o.customer_id = c.customer_id
               AND o.freight BETWEEN 50 AND 100);

SELECT company_name, contact_name
FROM customers c
WHERE NOT EXISTS(SELECT customer_id
                 FROM orders o
                 WHERE o.customer_id = c.customer_id
                   AND order_date BETWEEN '2015-02-01' AND '2015-02-15');

SELECT product_name
FROM products
WHERE NOT EXISTS(
        SELECT o.order_id
        FROM orders o
                 JOIN order_details od USING (order_id)
        WHERE o.order_date BETWEEN '1995-02-01' AND '1995-02-15');

-- nested queries with quantificators any, all

SELECT DISTINCT company_name --, p.product_name, SUM(od.quantity) AS quantity
FROM customers
         JOIN orders o ON customers.customer_id = o.customer_id
         JOIN order_details od ON o.order_id = od.order_id
         JOIN products p ON od.product_id = p.product_id
WHERE quantity > 40
-- GROUP BY company_name, p.product_name
ORDER BY company_name;

-- equivalent, but cant join with other table's fields
SELECT company_name
FROM customers
WHERE customer_id = ANY (
    SELECT DISTINCT customer_id
    FROM orders
             JOIN order_details od ON orders.order_id = od.order_id
    WHERE quantity > 40
);

SELECT AVG(quantity)
FROM order_details od;

SELECT product_name, quantity
FROM products
         JOIN order_details o ON products.product_id = o.product_id
WHERE quantity > (SELECT AVG(quantity)
                  FROM order_details od
)
ORDER BY quantity;

SELECT DISTINCT product_name, quantity
FROM products
         JOIN order_details od ON products.product_id = od.product_id
WHERE quantity > ALL (SELECT AVG(quantity)
                      FROM order_details
                      GROUP BY product_id)
ORDER BY quantity;

-- 1. Вывести продукты количество которых в продаже меньше самого малого среднего количества продуктов в деталях заказов (группировка по product_id). Результирующая таблица должна иметь колонки product_name и units_in_stock.
--
SELECT product_name, units_in_stock
FROM products
WHERE units_in_stock < ALL (
    SELECT AVG(quantity)
    FROM order_details
    GROUP BY product_id
)
ORDER BY units_in_stock DESC;

-- 2. Напишите запрос, который выводит общую сумму фрахтов заказов для компаний-заказчиков для заказов, стоимость фрахта которых больше средней величины стоимости фрахта всех заказов, а также дата отгрузки заказа должна находится во второй половине июля 1996 года. Результирующая таблица должна иметь колонки customer_id и freight_sum, строки которой должны быть отсортированы по сумме фрахтов заказов.
--
SELECT customer_id, SUM(freight) AS freight_sum
FROM orders
WHERE freight > (SELECT AVG(freight)
                 FROM orders)
  AND shipped_date BETWEEN '1996-07-16' AND '1996-07-31'
GROUP BY customer_id
ORDER BY freight_sum DESC;

-- Подсказка: таблицы можно соединять и с подзапросами (ведь подзапрос формирует, по сути, таблицу)
--
-- 3. Напишите запрос, который выводит 3 заказа с наибольшей стоимостью, которые были созданы после 1 сентября 1997
-- года включительно и были доставлены в страны Южной Америки. Общая стоимость рассчитывается как сумма стоимости
-- деталей заказа с учетом дисконта. Результирующая таблица должна иметь колонки customer_id, ship_country и order_price,
-- строки которой должны быть отсортированы по стоимости заказа в обратном порядке.
-- Страны Южной Америки:
-- 'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname',
-- 'Uruguay', 'Venezuela'.
--
SELECT customer_id, ship_country, order_price
FROM orders
         JOIN (SELECT order_id,
                      SUM(unit_price * quantity * (1 - discount)) AS order_price
               FROM order_details
               GROUP BY order_id) AS op
              USING (order_id)
WHERE ship_country IN
      ('Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname',
       'Uruguay', 'Venezuela')
  AND order_date >= '1997-09-01'
ORDER BY order_price DESC
LIMIT 3;

-- 4. Вывести все товары (уникальные названия продуктов), которых заказано ровно 10 единиц (конечно же, это можно
-- решить и без подзапроса).
SELECT DISTINCT product_name, quantity
FROM products
         JOIN order_details od ON products.product_id = od.product_id
WHERE quantity = 10;

SELECT DISTINCT product_name
FROM products
WHERE product_id =ANY( --IN ( --
    SELECT product_id
    FROM order_details
    WHERE quantity = 10
);
