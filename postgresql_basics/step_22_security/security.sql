DROP ROLE IF EXISTS sales_stuff;
CREATE ROLE sales_stuff;
DROP ROLE IF EXISTS northwind_admins;
CREATE ROLE northwind_admins;

DROP USER IF EXISTS john_smith;
CREATE USER john_smith WITH PASSWORD 'qwerty';
DROP USER IF EXISTS north_admin1;
CREATE USER north_admin1 WITH PASSWORD 'qwerty';
-- C:\Users\prape\pycharm\udemy\postgres_sql\step_22_security>psql northwind john_smith
-- Пароль пользователя john_smith:
-- psql (13.4)


REVOKE ALL ON DATABASE northwind FROM PUBLIC;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
-- C:\Users\prape\pycharm\udemy\postgres_sql\step_22_security>psql northwind john_smith
-- Пароль пользователя john_smith:
-- psql: ошибка: ВАЖНО:  доступ к базе "northwind" запрещён
-- ПОДРОБНОСТИ:  Пользователь не имеет привилегии CONNECT.

GRANT CONNECT ON DATABASE northwind TO sales_stuff;
GRANT CONNECT ON DATABASE northwind TO northwind_admins;

GRANT USAGE ON SCHEMA public TO sales_stuff;
GRANT USAGE ON SCHEMA public TO northwind_admins;

GRANT CREATE ON SCHEMA public TO northwind_admins;
GRANT CREATE ON DATABASE northwind TO northwind_admins;

GRANT sales_stuff TO john_smith;
GRANT northwind_admins TO north_admin1;

-- C:\Users\prape\pycharm\udemy\postgres_sql\step_22_security>psql northwind john_smith
-- northwind=> create table admin_demo2(admin_name varchar);
-- ОШИБКА:  нет доступа к схеме public

-- northwind=> insert into admin_demo1 values ('hello2');
-- ОШИБКА:  нет доступа к таблице admin_demo1


-- C:\Users\prape\pycharm\udemy\postgres_sql\step_22_security>psql northwind north_admin1
-- northwind=> create table admin_demo1(admin_name varchar);
-- CREATE TABLE
-- northwind=> insert into admin_demo1 values ('hello');
-- INSERT 0 1

SELECT grantee, privilege_type
FROM information_schema.role_table_grants
WHERE table_name = 'admin_demo1';
-- north_admin1,INSERT
-- north_admin1,SELECT
-- north_admin1,UPDATE
-- north_admin1,DELETE
-- north_admin1,TRUNCATE
-- north_admin1,REFERENCES
-- north_admin1,TRIGGER

GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA public TO northwind_admins;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE
    public.orders,
    public.order_details,
    public.products TO sales_stuff;
GRANT SELECT ON TABLE public.employees TO sales_stuff;

-- C:\Users\prape\pycharm\udemy\postgres_sql\step_22_security>psql northwind john_smith

-- northwind=> select address from employees;
--             address
-- --------------------------------
--  507 - 20th Ave. E.\nApt. 2A
--  908 W. Capital Way
--  722 Moss Bay Blvd.

-- northwind=> select * from customers;
-- ОШИБКА:  нет доступа к таблице customers
-- northwind=>

REVOKE SELECT ON employees FROM sales_stuff;
-- northwind=> select first_name from employees;
-- ОШИБКА:  нет доступа к таблице employees


GRANT SELECT (employee_id, title, title_of_courtesy, birth_date, hire_date, address, city,
              region, postal_code, country, home_phone, extension, photo, notes, reports_to,
              photo_path) ON employees TO sales_stuff;

-- northwind=> select address from employees;
--             address
-- --------------------------------
--  507 - 20th Ave. E.\nApt. 2A
--  908 W. Capital Way


-- northwind=> select first_name from employees;
-- ОШИБКА:  нет доступа к таблице employees

ALTER TABLE northwind.public.products
    ENABLE ROW LEVEL SECURITY;

-- northwind=> select count(*) from products;
--  count
-- -------
--      0

CREATE POLICY sales_active_products ON products
    FOR SELECT TO sales_stuff USING (northwind.public.products.discontinued <> 1);

-- northwind=> select count(*) from products;
--  count
-- -------
--     67

SELECT *
FROM northwind.public.products
WHERE reorder_level > 10;
-- 38
CREATE POLICY sales_active_products_2 ON products
    FOR SELECT TO sales_stuff USING (products.reorder_level > 10);
-- northwind=> select count(*) from products;
--  count
-- -------
--     68

-- northwind=> select count(*) from products where discontinued <> 1;
--  count
-- -------
--     67

DROP POLICY sales_active_products_2 ON northwind.public.products;
-- northwind=> select count(*) from products;
--  count
-- -------
--     67

REVOKE ALL PRIVILEGES ON northwind.public.employees, northwind.public.order_details FROM sales_stuff;
REVOKE ALL ON DATABASE northwind FROM sales_stuff;
REVOKE ALL ON SCHEMA public FROM sales_stuff;

DROP POLICY sales_active_products ON products;
DROP ROLE john_smith;
DROP ROLE sales_stuff;
SELECT * from pg_roles;