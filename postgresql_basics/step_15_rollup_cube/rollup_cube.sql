SELECT *
FROM products;

SELECT supplier_id, SUM(units_in_stock)
FROM products
GROUP BY supplier_id
ORDER BY supplier_id;


SELECT supplier_id, category_id, SUM(units_in_stock)
FROM products
GROUP BY supplier_id, category_id
ORDER BY supplier_id;

SELECT supplier_id, category_id, SUM(units_in_stock)
FROM products
GROUP BY GROUPING SETS ((supplier_id), (supplier_id, category_id))
ORDER BY supplier_id, category_id NULLS FIRST;

-- rollup

SELECT supplier_id, SUM(units_in_stock)
FROM products
GROUP BY ROLLUP (supplier_id)
ORDER BY supplier_id;

SELECT supplier_id, category_id, SUM(units_in_stock)
FROM products
GROUP BY ROLLUP (supplier_id, category_id)
ORDER BY supplier_id, category_id NULLS FIRST;


SELECT supplier_id, category_id, reorder_level, SUM(units_in_stock)
FROM products
GROUP BY ROLLUP (supplier_id, category_id, reorder_level)
ORDER BY supplier_id, category_id NULLS FIRST;

-- cube

SELECT supplier_id, category_id, SUM(units_in_stock)
FROM products
GROUP BY CUBE (supplier_id, category_id)
ORDER BY supplier_id, category_id NULLS FIRST;

-- homework
-- 1 Вывести сумму продаж (цена * кол-во) по каждому сотруднику с подсчётом полного итога (полной суммы по всем
-- сотрудникам) отсортировав по сумме продаж (по убыванию).
SELECT (e.first_name || ' ' || e.last_name) AS name, SUM(ROUND((unit_price * quantity)::NUMERIC, 2)) AS total
FROM orders
         JOIN order_details USING (order_id)
         JOIN employees e ON orders.employee_id = e.employee_id
GROUP BY ROLLUP (name)
ORDER BY total;


-- 2 Вывести отчёт показывающий сумму продаж по сотрудникам и странам отгрузки с подытогами по сотрудникам и общим итогом.
SELECT (e.first_name || ' ' || e.last_name)            AS name,
       ship_country,
       SUM(ROUND((unit_price * quantity)::NUMERIC, 2)) AS total
FROM orders
         JOIN order_details USING (order_id)
         JOIN employees e ON orders.employee_id = e.employee_id
GROUP BY ROLLUP (name, ship_country)
ORDER BY name, total NULLS LAST;



-- 3 Вывести отчёт показывающий сумму продаж по сотрудникам, странам отгрузки, сотрудникам и странам отгрузки с
-- подытогами по сотрудникам и общим итогом.

SELECT (e.first_name || ' ' || e.last_name)            AS name,
       ship_country,
       SUM(ROUND((unit_price * quantity)::NUMERIC, 2)) AS total
FROM orders
         JOIN order_details USING (order_id)
         JOIN employees e ON orders.employee_id = e.employee_id
GROUP BY CUBE (name, ship_country)
ORDER BY name, total NULLS LAST;
