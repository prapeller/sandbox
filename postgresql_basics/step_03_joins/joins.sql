-- inner join

SELECT p.product_name, p.units_in_stock, s.company_name
FROM products p
         INNER JOIN
     suppliers s
     ON p.supplier_id = s.supplier_id
ORDER BY p.units_in_stock DESC;

SELECT c.category_name, SUM(p.units_in_stock) AS qty_in_stock
FROM products p
         INNER JOIN
     categories c ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY qty_in_stock DESC
LIMIT 5;

SELECT c.category_name, ROUND(SUM(p.unit_price * p.units_in_stock)) AS total
FROM products p
         INNER JOIN
     categories c ON p.category_id = c.category_id
WHERE discontinued <> 1
GROUP BY c.category_name
HAVING SUM(p.unit_price * p.units_in_stock) > 5000
ORDER BY total DESC;

SELECT o.order_id, od.product_id, p.product_name, o.customer_id, first_name, last_name, title
FROM orders o
         JOIN order_details od ON o.order_id = od.order_id
         JOIN products p ON od.product_id = p.product_id
         JOIN employees e ON o.employee_id = e.employee_id;

SELECT contact_name,
       c.company_name,
       first_name,
       last_name,
       title,
       order_date,
       product_name,
       ship_country,
       p.unit_price,
       quantity,
       discount
FROM orders
         JOIN order_details od ON orders.order_id = od.order_id
--          JOIN shippers s ON s.shipper_id = orders.ship_via
         JOIN customers c ON orders.customer_id = c.customer_id
         JOIN products p ON od.product_id = p.product_id
         JOIN employees e ON orders.employee_id = e.employee_id;

-- left join, right join

SELECT company_name, product_name
FROM suppliers
         LEFT JOIN products p ON suppliers.supplier_id = p.supplier_id;

SELECT company_name, order_id
FROM customers c
         LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE order_id IS NULL;

SELECT company_name, order_id
FROM orders o
         RIGHT JOIN customers c ON c.customer_id = o.customer_id
WHERE order_id IS NULL;

SELECT COUNT(*)
FROM employees e
         LEFT JOIN orders o ON e.employee_id = o.employee_id
WHERE order_id IS NULL;

-- self join
CREATE TABLE employees_managers
(
    employee_id INT PRIMARY KEY,
    first_name  VARCHAR(255) NOT NULL,
    last_name   VARCHAR(255) NOT NULL,
    manager_id  INT,
    FOREIGN KEY (manager_id) REFERENCES employees_managers (employee_id)
);

INSERT INTO employees_managers (employee_id, first_name, last_name, manager_id)
VALUES (1, 'name1', 'last name1', NULL),
       (2, 'name2', 'last name2', 1),
       (3, 'name3', 'last name3', 1),
       (4, 'name4', 'last name4', 2),
       (5, 'name5', 'last name5', 2)
;

SELECT e.first_name || ' ' || e.last_name AS employee,
       m.first_name || ' ' || m.last_name AS manager
FROM employees_managers e
         LEFT JOIN employees_managers m ON e.manager_id = m.employee_id
ORDER BY manager;

-- using natural join

SELECT o.order_id, od.product_id, p.product_name, o.customer_id, first_name, last_name, title
FROM orders o
         JOIN order_details od USING (order_id) -- ON o.order_id = od.order_id
         JOIN products p USING (product_id) -- ON od.product_id = p.product_id
         JOIN employees e USING (employee_id);
-- ON o.employee_id = e.employee_id;

-- hw
-- 1. Найти заказчиков и обслуживающих их заказы сотрудников таких, что и заказчики и сотрудники из города London,
-- а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
-- Для вывода ФИО одним столбцом можно использовать в секции SELECT функцию CONCAT(first_name, ' ', last_name), которая
-- "склеивает" строчные аргументы.
--
SELECT c.company_name, CONCAT(e.first_name, ' ', e.last_name) AS employee
FROM customers c
         JOIN orders o ON c.customer_id = o.customer_id
         JOIN employees e ON o.employee_id = e.employee_id
         JOIN shippers s ON o.ship_via = s.shipper_id
WHERE c.city = 'London'
  AND e.city = 'London'
  AND s.company_name = 'Speedy Express';

-- 2. Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20
-- единиц. Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.
--
SELECT product_name, units_in_stock, s.contact_name, phone
FROM suppliers s
         JOIN products p ON s.supplier_id = p.supplier_id
         JOIN categories c ON p.category_id = c.category_id
WHERE discontinued = 0
  AND units_in_stock < 20
  AND category_name IN ('Beverages', 'Seafood')
ORDER BY units_in_stock DESC;

-- 3. Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
--
SELECT company_name, contact_name, order_id
FROM customers
         LEFT JOIN orders o ON customers.customer_id = o.customer_id
WHERE order_id IS NULL;

-- 4. Переписать предыдущий запрос, использовав симметричный вид джойна (подсказка: речь о LEFT и RIGHT).
SELECT company_name, order_id
FROM orders
         RIGHT JOIN customers ON orders.customer_id = customers.customer_id
WHERE order_id IS NULL;