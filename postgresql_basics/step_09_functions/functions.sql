-- without args

SELECT *
FROM customers;

DROP TABLE IF EXISTS tmp_customers;

SELECT *
INTO tmp_customers
FROM customers;

SELECT *
FROM tmp_customers;


CREATE OR REPLACE FUNCTION fix_customer_region() RETURNS VOID AS
$$
UPDATE tmp_customers
SET region = 'unknown'
WHERE region IS NULL
$$
    LANGUAGE sql;

SELECT fix_customer_region();


-- returns (1 value), scalar
CREATE OR REPLACE FUNCTION get_total_number_of_goods() RETURNS BIGINT AS
$$
SELECT SUM(units_in_stock)
FROM products
$$
    LANGUAGE sql;

SELECT get_total_number_of_goods() AS total_goods;

CREATE OR REPLACE FUNCTION get_avg_price() RETURNS float8 AS
$$
SELECT AVG(unit_price)
FROM products
$$
    LANGUAGE sql;

SELECT get_avg_price() AS avg_price;


-- in, out, default, inout, variadic

-- in (1 value) returns (1 value)
DROP FUNCTION get_product_price_by_name;
CREATE OR REPLACE FUNCTION get_product_price_by_name(IN prod_name VARCHAR) RETURNS TEXT AS
$$
SELECT CONCAT(product_name, unit_price)
FROM products
WHERE LOWER(product_name) LIKE CONCAT('%', LOWER(prod_name), '%')
$$
    LANGUAGE sql;

SELECT get_product_price_by_name('chocola') AS price;
SELECT get_product_price_by_name('chocolad') AS price;

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

-- in (1 value) out (2 values (first true row))
CREATE OR REPLACE FUNCTION get_price_boundaries_by_discountinuity(is_disc INT, OUT max_price REAL, OUT min_price REAL) AS
$$
SELECT MAX(unit_price), MIN(unit_price)
FROM products
WHERE discontinued = is_disc
$$
    LANGUAGE sql;

SELECT get_price_boundaries_by_discountinuity(0);
SELECT *
FROM get_price_boundaries_by_discountinuity(1);

-- -- in (1 value (default)) out (2 values (first true row))
CREATE OR REPLACE FUNCTION get_price_boundaries_by_discountinuity(is_disc INT DEFAULT 1, OUT max_price REAL, OUT min_price REAL) AS
$$
SELECT MAX(unit_price), MIN(unit_price)
FROM products
WHERE discontinued = is_disc
$$
    LANGUAGE sql;

SELECT get_price_boundaries_by_discountinuity(0);
SELECT *
FROM get_price_boundaries_by_discountinuity();

-- returns setof values
CREATE OR REPLACE FUNCTION get_avg_prices_by_categories() RETURNS SETOF DOUBLE PRECISION AS
$$
SELECT AVG(unit_price)
FROM products
GROUP BY category_id

$$ LANGUAGE SQL;

SELECT get_avg_prices_by_categories() AS avg_price;


-- (out 2 values) returns setof record (with those 2 values)
DROP FUNCTION get_avg_prices_by_prod_cats;
CREATE OR REPLACE FUNCTION get_avg_prices_by_prod_cats(OUT cat VARCHAR, OUT avg_price float8)
    RETURNS SETOF RECORD AS
$$
SELECT category_name, AVG(unit_price)
FROM products
         JOIN categories c ON products.category_id = c.category_id
GROUP BY category_name

$$ LANGUAGE SQL;

SELECT get_avg_prices_by_prod_cats() AS avg_price;

SELECT *
FROM get_avg_prices_by_prod_cats();

SELECT cat AS category, avg_price AS average_price
FROM get_avg_prices_by_prod_cats();

-- setof record (without outs)
DROP FUNCTION get_avg_prices_by_prod_cats;
CREATE OR REPLACE FUNCTION get_avg_prices_by_prod_cats()
    RETURNS SETOF RECORD AS
$$
SELECT category_name, AVG(unit_price)
FROM products
         JOIN categories c ON products.category_id = c.category_id
GROUP BY category_name
$$ LANGUAGE SQL;

-- SELECT avg_price
-- FROM get_avg_prices_by_prod_cats();
--
-- SELECT category_name, avg_price
-- FROM get_avg_prices_by_prod_cats();

-- SELECT * FROM get_avg_prices_by_prod_cats();

-- SELECT cat AS category, avg_price AS average_price
-- FROM get_avg_prices_by_prod_cats();

SELECT *
FROM get_avg_prices_by_prod_cats() AS (cat_name VARCHAR, av_pr float8);

SELECT get_avg_prices_by_prod_cats() AS cat_name_avg_price;


-- returns table
CREATE OR REPLACE FUNCTION get_customers_by_country(customer_country VARCHAR)
    RETURNS TABLE
            (
                char_code    CHAR,
                company_name VARCHAR
            )
AS
$$
SELECT customer_id, company_name
FROM customers
WHERE country = customer_country
$$
    LANGUAGE sql;

SELECT *
FROM get_customers_by_country('USA');

SELECT company_name
FROM get_customers_by_country('USA');

SELECT char_code, company_name
FROM get_customers_by_country('USA');

-- SELECT customer_id, company_name
-- FROM get_customers_by_country('USA');


-- in (1 value) returns setof (table)
DROP FUNCTION get_customers_by_country;
CREATE OR REPLACE FUNCTION get_customers_by_country(customer_country VARCHAR)
    RETURNS SETOF customers
    --             (
--                 char_code    CHAR,
--                 company_name VARCHAR
--             )
AS
$$

    -- SELECT customer_id, company_name
-- FROM customers
-- WHERE country = customer_country

SELECT *
FROM customers
WHERE country = customer_country
$$
    LANGUAGE sql;

SELECT *
FROM get_customers_by_country('USA');

SELECT company_name
FROM get_customers_by_country('USA');

-- SELECT char_code, company_name
-- FROM get_customers_by_country('USA');

SELECT customer_id, company_name
FROM get_customers_by_country('USA');


-- plpgsql


-- returns (1 value) scalar
CREATE OR REPLACE FUNCTION get_total_number_of_goods() RETURNS BIGINT AS
$$
BEGIN
    RETURN SUM(units_in_stock) FROM products;
END
$$ LANGUAGE plpgsql;

SELECT get_total_number_of_goods();



CREATE OR REPLACE FUNCTION get_max_price_from_discontinued() RETURNS REAL AS
$$
BEGIN
    RETURN MAX(unit_price) FROM products WHERE discontinued = 1;
END
$$ LANGUAGE plpgsql;

SELECT get_max_price_from_discontinued();


-- out (2 values)
CREATE OR REPLACE FUNCTION get_price_bndrs(OUT max_price REAL, OUT min_price REAL) AS
$$
BEGIN
    --     max_price := MAX(unit_price) FROM products;
    --     min_price := MIN(unit_price) FROM products;
    SELECT MAX(unit_price), MIN(unit_price) INTO max_price, min_price FROM products;
END
$$ LANGUAGE plpgsql;

-- record
SELECT get_price_bndrs();
-- fields
SELECT *
FROM get_price_bndrs();

-- in (2 values) out (1 value)
CREATE OR REPLACE FUNCTION get_sum(x INT, y INT, OUT sum INT) AS
$$
BEGIN
    sum := x + y;
    RETURN;
END
$$ LANGUAGE plpgsql;

SELECT *
FROM get_sum(2, 3);

-- returns setof (table)
DROP FUNCTION get_customers_by_country;
CREATE OR REPLACE FUNCTION get_customers_by_country(cust_country VARCHAR) RETURNS SETOF customers AS
$$
BEGIN
    RETURN QUERY
        SELECT *
        FROM customers
        WHERE country = cust_country;
END
$$ LANGUAGE plpgsql;

SELECT *
FROM get_customers_by_country('USA');


-- in (3 values) returns (1 value)
-- declare
CREATE OR REPLACE FUNCTION get_square(ab REAL, bc REAL, ac REAL) RETURNS REAL AS
$$
DECLARE
    half_per REAL;
BEGIN
    half_per = (ab + bc + ac) / 2;
    RETURN SQRT(half_per * (half_per - ab) * (half_per - bc) * (half_per - ac));
END;

$$ LANGUAGE plpgsql;

SELECT get_square(6, 6, 6);


-- returns setof (table)
DROP FUNCTION get_middle_price_products;
CREATE FUNCTION get_middle_price_products() RETURNS SETOF products AS
$$
DECLARE
    avg_price  REAL;
    low_price  REAL;
    high_price REAL;
BEGIN
    SELECT AVG(unit_price)
    INTO avg_price
    FROM products;

    low_price = avg_price * 0.75;
    high_price = avg_price * 1.25;

    RETURN QUERY
        SELECT *
        FROM products
        WHERE unit_price BETWEEN low_price AND high_price;
END
$$ LANGUAGE plpgsql;

SELECT product_name, unit_price
FROM get_middle_price_products();

-- if else
CREATE OR REPLACE FUNCTION conver_temp_to(temp REAL, to_celsius bool DEFAULT TRUE) RETURNS REAL AS
$$
DECLARE
    result_temp REAL;
BEGIN
    IF to_celsius THEN
        result_temp = (5.0 / 9.0) * (temp - 32);
    ELSE
        result_temp = (9.0 * temp + (32 * 5)) / 5.0;
    END IF;

    RETURN result_temp;
END;
$$ LANGUAGE plpgsql;

SELECT conver_temp_to(80);
SELECT conver_temp_to(26.6, FALSE);

CREATE FUNCTION get_season(month_number INT) RETURNS TEXT AS
$$
DECLARE
    season VARCHAR(10);
BEGIN
    IF month_number BETWEEN 3 AND 5 THEN
        season = 'Spring';
    ELSEIF month_number BETWEEN 6 AND 8 THEN
        season = 'Summer';
    ELSEIF month_number BETWEEN 9 AND 11 THEN
        season = 'Autumn';
    ELSE
        season = 'Winter';
    END IF;
    RETURN season;
END;
$$ LANGUAGE plpgsql;

SELECT get_season(4);


-- cycles
CREATE OR REPLACE FUNCTION fib(n INT) RETURNS INT AS
$$
DECLARE
    counter INT = 0;
    i       INT = 0;
    j       INT = 1;
BEGIN
    IF
        n < 1 THEN
        RETURN 0;
    END IF;

    WHILE counter < n
        LOOP
            counter = counter + 1;
            SELECT j, i + j INTO i, j;
        END LOOP;
    RETURN i;
END;
$$ LANGUAGE plpgsql;

SELECT fib(5);


CREATE OR REPLACE FUNCTION fib(n INT) RETURNS INT AS
$$
DECLARE
    counter INT = 0;
    i       INT = 0;
    j       INT = 1;
BEGIN
    IF
        n < 1 THEN
        RETURN 0;
    END IF;

    LOOP
        EXIT WHEN counter > n;
        counter = counter + 1;
        SELECT j, i + j INTO i, j;
    END LOOP;

    RETURN i;
END;

$$ LANGUAGE plpgsql;

SELECT fib(4);

DO
$$
    BEGIN
        FOR counter IN 1..5
            LOOP
                RAISE NOTICE 'counter: %', counter;
            END LOOP;
    END;
$$;

DO
$$
    BEGIN
        FOR counter IN REVERSE 10..1 BY 2
            LOOP
                RAISE NOTICE 'counter: %', counter;
            END LOOP;
    END;
$$;


-- return next (rare usage)
CREATE FUNCTION return_ints() RETURNS SETOF INT AS
$$
BEGIN
    RETURN NEXT 1;
    RETURN NEXT 2;
    RETURN NEXT 3;
--     RETURN
END;
$$ LANGUAGE plpgsql;

SELECT *
FROM return_ints();

-- homework
-- 1. Создайте функцию, которая делает бэкап таблицы customers (копирует все данные в другую таблицу), предварительно
-- стирая таблицу для бэкапа, если такая уже существует (чтобы в случае многократного запуска таблица для бэкапа перезатиралась).

DROP FUNCTION IF EXISTS backup();
DROP TABLE IF EXISTS customers_bckp;
CREATE OR REPLACE FUNCTION backup() RETURNS VOID AS
$$
DROP TABLE IF EXISTS customers_bckp;
    -- SELECT *
    -- INTO customers_bckp
    -- FROM customers;

    CREATE TABLE customers_bckp AS
    SELECT *
    FROM customers;

    $$ LANGUAGE sql;

SELECT backup();
SELECT *
FROM customers_bckp;

-- 2. Создать функцию, которая возвращает средний фрахт (freight) по всем заказам

CREATE OR REPLACE FUNCTION get_avg_freight() RETURNS float8 AS
$$
SELECT AVG(freight)
FROM orders;
$$
    LANGUAGE sql;

SELECT get_avg_freight();

-- 3. Написать функцию, которая принимает два целочисленных параметра, используемых как нижняя и верхняя границы для генерации случайного числа в пределах этой границы (включая сами граничные значения).
-- Функция random генерирует вещественное число от 0 до 1.
-- Необходимо вычислить разницу между границами и прибавить единицу.
-- На полученное число умножить результат функции random() и прибавить к результату значение нижней границы.
-- Применить функцию floor() к конечному результату, чтобы не "уехать" за границу и получить целое число.

DROP FUNCTION IF EXISTS get_random_withing_bndrs;
CREATE OR REPLACE FUNCTION get_random_withing_bndrs(bottom INT, up INT) RETURNS INT AS
$$
SELECT FLOOR(bottom + RANDOM() * (up - bottom + 1));
$$
    LANGUAGE sql;

SELECT get_random_withing_bndrs(3, 10)
FROM GENERATE_SERIES(1, 10);

-- Перед выполнением заданий 4-9, загрузить скрипт по ссылке: https://1drv.ms/u/s!AqtQeAOHZEjQvLgOEzFOSRxVzHJn8Q?e=KloNsI и исполнить его, создав подключение к БД Northwind. Этот скрипт добавляет столбец salary в таблицу employees.
-- 4. Создать функцию, которая возвращает самые низкую и высокую зарплаты среди сотрудников заданного города

DROP FUNCTION IF EXISTS get_lowest_highers_sal_by_city;
CREATE OR REPLACE FUNCTION get_lowest_highers_sal_by_city(u_city VARCHAR, OUT min_sal NUMERIC, OUT max_sal NUMERIC) AS
$$
BEGIN
    SELECT MIN(salary), MAX(salary) INTO min_sal, max_sal FROM employees WHERE city = u_city;
END;
$$
    LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS get_lowest_highers_sal_by_city;
CREATE OR REPLACE FUNCTION get_lowest_highers_sal_by_city(u_city VARCHAR, OUT min_sal NUMERIC, OUT max_sal NUMERIC) AS
$$
SELECT MIN(salary), MAX(salary)
FROM employees
WHERE city = u_city;
$$
    LANGUAGE sql;

SELECT get_lowest_highers_sal_by_city('London');

SELECT min_sal AS minimum_salary, max_sal AS maximum_salary
FROM get_lowest_highers_sal_by_city('Seattle');

-- 5. Создать функцию, которая корректирует зарплату на заданный процент,  но не корректирует зарплату, если её уровень
-- превышает заданный уровень при этом верхний уровень зарплаты по умолчанию равен 70, а процент коррекции равен 15%.


CREATE OR REPLACE FUNCTION correct_salary_to(percent FLOAT DEFAULT 1, upper NUMERIC DEFAULT 70.00) RETURNS VOID AS
$$
UPDATE employees
SET salary = salary * percent
WHERE salary <= upper
$$
    LANGUAGE sql;

SELECT correct_salary_to(1.2);

-- 6. Модифицировать функцию, корректирующую зарплату таким образом, чтобы в результате коррекции, она так же выводила бы изменённые записи.

DROP FUNCTION correct_and_display_salary_to;
CREATE OR REPLACE FUNCTION correct_and_display_salary_to(percent FLOAT DEFAULT 1, upper NUMERIC DEFAULT 70.00)
    RETURNS SETOF employees AS
$$
UPDATE employees
SET salary = salary * percent
WHERE salary <= upper
RETURNING *;
$$
    LANGUAGE sql;

SELECT *
FROM correct_and_display_salary_to(1.2);

-- 7. Модифицировать предыдущую функцию так, чтобы она возвращала только колонки last_name, first_name, title, salary

DROP FUNCTION correct_and_display_salary_to;
CREATE OR REPLACE FUNCTION correct_and_display_salary_to(percent FLOAT DEFAULT 1, upper NUMERIC DEFAULT 70.00,
                                                         OUT last_name VARCHAR, OUT first_name VARCHAR,
                                                         OUT title VARCHAR, OUT salary NUMERIC) RETURNS SETOF RECORD AS
$$
UPDATE employees
SET salary = salary * percent
WHERE salary <= upper;

SELECT last_name, first_name, title, salary
FROM employees;

$$
    LANGUAGE sql;

SELECT *
FROM correct_and_display_salary_to(1.2);

DROP FUNCTION correct_and_display_salary_to;
CREATE OR REPLACE FUNCTION correct_and_display_salary_to(percent FLOAT DEFAULT 1, upper NUMERIC DEFAULT 70.00)
    RETURNS TABLE
            (
                last_name  VARCHAR,
                first_name VARCHAR,
                title      VARCHAR,
                salary     NUMERIC
            )
AS
$$
UPDATE employees
SET salary = salary * percent
WHERE salary <= upper
RETURNING last_name, first_name, title, salary;

    -- SELECT last_name, first_name, title, salary
-- FROM employees;

$$
    LANGUAGE sql;

SELECT *
FROM correct_and_display_salary_to(1.2);

-- 8. Написать функцию, которая принимает метод доставки и возвращает записи из таблицы orders в которых freight меньше значения, определяемого по следующему алгоритму:
-- - ищем максимум фрахта (freight) среди заказов по заданному методу доставки
-- - корректируем найденный максимум на 30% в сторону понижения
-- - вычисляем среднее значение фрахта среди заказов по заданному методу доставки
-- - вычисляем среднее значение между средним найденным на предыдущем шаге и скорректированным максимумом
-- - возвращаем все заказы в которых значение фрахта меньше найденного на предыдущем шаге среднего

DROP FUNCTION get_orders_with_lower_freight;
CREATE OR REPLACE FUNCTION get_orders_with_lower_freight(u_ship_via INT) RETURNS SETOF orders AS
$$
DECLARE
    max_freight         NUMERIC;
    lowered_max_freight NUMERIC;
    avg_freight         NUMERIC;
    avg_lowered_freight NUMERIC;
BEGIN
    max_freight := MAX(freight) FROM orders WHERE ship_via = u_ship_via;
    lowered_max_freight := max_freight * 0.7;
    avg_freight := AVG(freight) FROM orders WHERE ship_via = u_ship_via;
    avg_lowered_freight := (lowered_max_freight + avg_freight) / 2;
    RETURN QUERY
        SELECT * FROM orders WHERE freight < avg_lowered_freight;
END;
$$
    LANGUAGE plpgsql;

SELECT COUNT(*)
FROM get_orders_with_lower_freight(1);

-- 9. Написать функцию, которая принимает:
-- уровень зарплаты, максимальную зарплату (по умолчанию 80) минимальную зарплату (по умолчанию 30), коээфициент роста зарплаты (по умолчанию 20%)
-- Если зарплата выше минимальной, то возвращает false
-- Если зарплата ниже минимальной, то увеличивает зарплату на коэффициент роста и проверяет не станет ли зарплата после
-- повышения превышать максимальную.
-- Если превысит - возвращает false, в противном случае true.
-- Проверить реализацию, передавая следующие параметры
-- (где c - уровень з/п, max - макс. уровень з/п, min - минимальный уровень з/п, r - коэффициент):
-- c = 40, max = 80, min = 30, r = 0.2 - должна вернуть false
-- c = 79, max = 81, min = 80, r = 0.2 - должна вернуть false
-- c = 79, max = 95, min = 80, r = 0.2 - должна вернуть true

CREATE OR REPLACE FUNCTION should_increase(cur_sal NUMERIC, max_sal NUMERIC DEFAULT 80, min_sal NUMERIC DEFAULT 30,
                                          raise_rate FLOAT DEFAULT 1.2) RETURNS bool AS
$$
DECLARE
    result bool;
BEGIN
    IF cur_sal > min_sal THEN
        result := FALSE;
    ELSEIF cur_sal < min_sal THEN
        cur_sal = cur_sal * raise_rate;
        IF cur_sal > max_sal THEN
            result := FALSE;
        ELSE
            result := TRUE;
        END IF;
    END IF;
    RETURN result;
END;
$$
    LANGUAGE plpgsql;

SELECT should_increase(40, 80, 30, 1.2);
SELECT should_increase(79, 81, 80, 1.2);
SELECT should_increase(79, 95, 80, 1.2);
