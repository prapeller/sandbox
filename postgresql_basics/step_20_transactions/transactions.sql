-- ACID:

-- Atomicity - no transaction registered partially, all or nothing (rollback)
-- Consistency - all data are consistent (if somewhere theres plus, somewhere should be minus)
-- Isolation - parallel operations cannot have effect to that transaction (when somewhere one plus, somewhere should be only one minus)
--         solves such problems with parallel operations
--             -dirty reading - parallel can see uncommitted changes and
--             -not repeating reading - second reading (before start) see different result (before end) during UPDATE transaction
--             -fantom reading - same as 'not repeating' but for INSERT/DELETE transactions
--             -serialisation anomaly - result of parallel operations <> result of operations going one by one

-- Durability - if transaction succeed, no rollback possible

-- TCL - transaction control language
-- a)standard sql: begin / commit
-- b)postgres sql: start transaction / end
-- savepoint

BEGIN;-- (default read commited)
WITH prod_update AS (
    UPDATE products
        SET discontinued = 1
        WHERE units_in_stock < 10
        RETURNING product_id
)
SELECT *
INTO last_orders_on_discontinued
FROM order_details
WHERE product_id IN (SELECT product_id FROM prod_update);
DROP TABLE last_orders_on_discontinued1;
-- ROLLBACK;
COMMIT;


SELECT *
FROM last_orders_on_discontinued;

DROP TABLE IF EXISTS last_orders_on_discontinued;


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

WITH prod_update AS (
    UPDATE products
        SET discontinued = 1
        WHERE units_in_stock < 10
        RETURNING product_id
)
SELECT *
INTO last_orders_on_discontinued
FROM order_details
WHERE product_id IN (SELECT product_id FROM prod_update);
SAVEPOINT backup;

SELECT COUNT(*)
FROM order_details;

DELETE
FROM order_details
WHERE product_id IN (SELECT product_id FROM last_orders_on_discontinued);

SELECT COUNT(*)
FROM order_details;

ROLLBACK TO backup; -- its possible to call this rollback from upper language app (i.e. python app)

SELECT COUNT(*)
FROM order_details;
SELECT *
FROM last_orders_on_discontinued;

UPDATE order_details
SET quantity = 0
WHERE product_id IN (SELECT product_id FROM last_orders_on_discontinued);

COMMIT;

-- DROP TABLE IF EXISTS last_orders_on_discontinued;

SELECT *
FROM order_details
WHERE product_id IN (SELECT product_id FROM last_orders_on_discontinued);

-- 1. В рамках транзакции с уровнем изоляции Repeatable Read выполнить следующие операции:
-- - заархивировать (SELECT INTO или CREATE TABLE AS) заказчиков, которые сделали покупок менее чем на 2000 у.е.
-- - удалить из таблицы заказчиков всех заказчиков, которые были предварительно заархивированы (подсказка: для этого придётся удалить данные из связанных таблиц)

BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
DROP TABLE IF EXISTS archive_poor_customers;

CREATE TABLE archive_poor_customers AS
SELECT company_name, SUM(unit_price * quantity) AS total
FROM orders
         JOIN order_details od ON orders.order_id = od.order_id
         JOIN customers c ON orders.customer_id = c.customer_id
GROUP BY company_name
HAVING SUM(unit_price * quantity) < 2000
ORDER BY SUM(unit_price * quantity) DESC;

-- ROLLBACK;

DELETE
FROM order_details
WHERE order_id IN (
    SELECT order_id
    FROM orders
    WHERE customer_id IN (SELECT customer_id FROM archive_poor_customers)
)
;

DELETE
FROM orders
WHERE customer_id IN (SELECT customer_id FROM archive_poor_customers);

DELETE
FROM customers
WHERE customer_id IN (SELECT customer_id FROM archive_poor_customers);

COMMIT;

SELECT *
FROM archive_poor_customers;


-- 2. В рамках транзакции выполнить следующие операции:
-- - заархивировать все продукты, снятые с продажи (см. колонку discontinued)
-- - поставить savepoint после архивации
-- - удалить из таблицы продуктов все продукты, которые были заархивированы
-- - откатиться к savepoint
-- - закоммитить тразнакцию
