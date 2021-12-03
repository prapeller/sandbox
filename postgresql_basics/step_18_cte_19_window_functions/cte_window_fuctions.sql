SELECT company_name
FROM suppliers
WHERE country IN (SELECT country FROM customers);

WITH customer_courtries AS (SELECT country FROM customers)
SELECT company_name
FROM suppliers
WHERE country IN (SELECT * FROM customer_courtries);

SELECT company_name
FROM suppliers s
WHERE NOT EXISTS(SELECT p.product_id
                 FROM products p
                          JOIN order_details od ON p.product_id = od.product_id
                          JOIN orders o ON od.order_id = o.order_id
                 WHERE s.supplier_id = p.supplier_id
                   AND o.order_date BETWEEN '1998-02-01' AND '1998-02-04');

WITH filtered AS (SELECT company_name, supplier_id
                  FROM products p
                           JOIN order_details USING (product_id)
                           JOIN orders USING (order_id)
                           JOIN suppliers USING (supplier_id)
                  WHERE order_date BETWEEN '1998-02-01' AND '1998-02-04')
SELECT company_name
FROM suppliers s
WHERE supplier_id NOT IN (SELECT supplier_id FROM filtered);

-- recursive

DROP TABLE IF EXISTS employee;
CREATE TABLE employee
(
    id      SERIAL PRIMARY KEY,
    name    VARCHAR NOT NULL,
    boss_id INT,
    FOREIGN KEY (boss_id) REFERENCES employee (id) ON DELETE CASCADE
);

INSERT INTO employee (name, boss_id)
VALUES ('windy', NULL),
       ('shmindy', 1),
       ('bossom', 1),
       ('shmossom', 2),
       ('hobbit', 2),
       ('shmobbit', 3),
       ('shirley', 3),
       ('mirley', 4);

SELECT emp.name, boss.name
FROM employee emp
         LEFT JOIN employee boss ON emp.boss_id = boss.id
ORDER BY boss.name;

WITH RECURSIVE submission(sub_line, id) AS
                   (
                       SELECT name, id
                       FROM employee
                       WHERE boss_id IS NULL
                       UNION ALL
                       SELECT sub_line || ' -> ' || e.name, e.id
                       FROM employee e,
                            submission s
                       WHERE e.boss_id = s.id
                   )
SELECT *
FROM submission;

-- window functions: over(partition by ... order by)
--     aggregation: sum, avg, min, max, count
--     ranging: row_number, rank, lag, lead

SELECT category_name, ROUND(AVG(unit_price)::NUMERIC, 2) average_price
FROM products
         JOIN categories c ON products.category_id = c.category_id
GROUP BY category_name
ORDER BY average_price;

SELECT category_name,
       product_name,
       unit_price,
--        AVG(unit_price)
       AVG(unit_price) OVER (PARTITION BY category_id) AS average_price
FROM products
         JOIN categories USING (category_id);
-- GROUP BY category_name, product_name, unit_price

SELECT o.order_id,
       p.product_name,
       od.unit_price,
       od.quantity,
       SUM(od.unit_price * od.quantity) OVER (PARTITION BY o.order_id) AS sale_sum
FROM orders o
         JOIN order_details od ON o.order_id = od.order_id
         JOIN products p ON od.product_id = p.product_id;

SELECT o.order_id,
       p.product_name,
       od.unit_price,
       od.quantity,
       SUM(od.unit_price * od.quantity) OVER (PARTITION BY o.order_id ORDER BY p.product_name) AS sale_sum
FROM orders o
         JOIN order_details od ON o.order_id = od.order_id
         JOIN products p ON od.product_id = p.product_id;

-- with increasing sale_sum by product_name inside each order_id
SELECT o.order_id,
       p.product_name,
       od.unit_price,
       od.quantity,
       SUM(od.unit_price * od.quantity) OVER (PARTITION BY o.order_id ORDER BY p.product_name) AS sale_sum
FROM orders o
         JOIN order_details od ON o.order_id = od.order_id
         JOIN products p ON od.product_id = p.product_id
ORDER BY o.order_id;

-- if want to have increased sale_sum by each product inside all orders
-- row_number:
SELECT row_id,
       order_id,
       product_name,
       customer_id,
       unit_price,
       SUM(unit_price) OVER (ORDER BY row_id) AS cascade_total
FROM (
         SELECT order_id, product_name, customer_id, od.unit_price, ROW_NUMBER() OVER () AS row_id
         FROM orders
                  JOIN order_details od USING (order_id)
                  JOIN products USING (product_id)
     ) subquery;

-- rank

SELECT product_name,
       units_in_stock,
       RANK() OVER (ORDER BY product_id)
FROM products;

SELECT product_name, units_in_stock, RANK() OVER (ORDER BY units_in_stock)
FROM products;

-- dense_rank

SELECT product_name, units_in_stock, DENSE_RANK() OVER (ORDER BY units_in_stock)
FROM products;

SELECT product_name,
       unit_price,
       DENSE_RANK() OVER (
           ORDER BY
               CASE
                   WHEN unit_price > 80 THEN 1
                   WHEN unit_price > 30 AND unit_price < 80 THEN 2
                   ELSE 3
                   END
           ) AS ranking
FROM products
ORDER BY unit_price DESC;

-- lag

SELECT product_name,
       unit_price,
       LAG(unit_price) OVER (ORDER BY unit_price DESC) - unit_price AS price_lag
FROM products
ORDER BY unit_price DESC;

-- lead

SELECT product_name,
       unit_price,
       LEAD(unit_price, 3) OVER (ORDER BY unit_price) - unit_price AS price_lag
FROM products
ORDER BY unit_price DESC;

-- nth numbers
SELECT *
FROM products
WHERE product_id = ANY (
    SELECT product_id
    FROM (
             SELECT product_id, unit_price, ROW_NUMBER() OVER (ORDER BY unit_price DESC) AS nth
             FROM products
         ) sorted_prices
    WHERE nth < 4
);

-- homework

-- Вывести отчёт показывающий по сотрудникам суммы продаж SUM(unit_price*quantity), и сопоставляющий их со средним
-- значением суммы продаж по сотрудникам (AVG по SUM(unit_price*quantity)) сортированный по сумме продаж по убыванию.

SELECT DISTINCT employee_id, total_over_employee, AVG(total_over_employee) OVER () AS average_sales
FROM (
         SELECT employee_id, SUM(unit_price * quantity) OVER (PARTITION BY employee_id) AS total_over_employee
         FROM orders
                  JOIN order_details USING (order_id)
     ) q
ORDER BY total_over_employee DESC;

-- Вывести ранг сотрудников по их зарплате, без пропусков. Также вывести имя, фамилию и должность.

SELECT last_name, first_name, salary, title, RANK() OVER (ORDER BY salary desc)
from employees