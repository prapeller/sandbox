-- create trigger trigger_name() conditino on table_name
--     for each row execute procedure function_name();

-- trigger creation:
-- CREATE FUNCTION func_name() RETURNS TRIGGER AS
-- $$
-- BEGIN
--
-- END;
-- $$ LANGUAGE plpgsql;

--     create trigger trigger_name() on table_name
--     referencing [new/old] table as ref_table_name
--     for each statement execute procedure function_name()

ALTER TABLE customers
    DROP COLUMN IF EXISTS last_updated;

ALTER TABLE customers
    ADD COLUMN last_updated TIMESTAMP;

-- drop FUNCTION IF EXISTS customers_timestamp CASCADE;
-- drop FUNCTION IF EXISTS customers_timestamp_function CASCADE;

-- INSERT INTO customers (SELECT * FROM customers_bckp);

CREATE OR REPLACE FUNCTION customers_timestamp_function() RETURNS TRIGGER AS
$$
BEGIN
    new.last_updated = NOW();
    RETURN new;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS customers_timestamp_trigger ON customers;
CREATE TRIGGER customers_timestamp_trigger
    BEFORE INSERT OR UPDATE
    ON customers
    FOR EACH ROW
EXECUTE PROCEDURE customers_timestamp_function();


SELECT *
FROM customers;

UPDATE customers
SET address = 'blabla'
WHERE customer_id = 'ALFKI';

INSERT INTO customers
VALUES ('asdf', 'comp', 'cont', 'titl', 'add', 'city', NULL, 'code', 'count', '', '', NULL);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


ALTER TABLE employees
    ADD COLUMN user_changed TEXT;

CREATE OR REPLACE FUNCTION changes_on_employees_function() RETURNS TRIGGER AS
$$
BEGIN
    new.user_changed = SESSION_USER;
    RETURN new;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS changes_on_employees_trigger ON employees;
CREATE TRIGGER changes_on_employees_trigger
    BEFORE INSERT OR UPDATE
    ON employees
    FOR EACH ROW
EXECUTE PROCEDURE changes_on_employees_function();

SELECT *
FROM employees;

UPDATE employees
SET salary = 88
WHERE employee_id = 1;

INSERT INTO employees
VALUES ('10', '', '', '', '', NULL, NULL, '', '', '', '', '', '', '', NULL, '', NULL, '', 0, NULL);

SELECT *
FROM employees;


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- table audit
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

DROP TABLE IF EXISTS products_audit;

CREATE TABLE products_audit
(
    op                CHAR(1)                                              NOT NULL,
    user_changed      TEXT                                                 NOT NULL,
    time_stamp        TIMESTAMP                                            NOT NULL,

    product_id        SMALLINT DEFAULT NEXTVAL('product_id_seq'::regclass) NOT NULL
        CONSTRAINT pk_products2
            PRIMARY KEY,
    product_name      VARCHAR(40)                                          NOT NULL,
    supplier_id       SMALLINT
        CONSTRAINT fk_products_suppliers2
            REFERENCES suppliers,
    category_id       SMALLINT
        CONSTRAINT fk_products_categories2
            REFERENCES categories,
    quantity_per_unit VARCHAR(20),
    unit_price        REAL
        CONSTRAINT chk_unit_price2
            CHECK (unit_price > (0)::DOUBLE PRECISION),
    units_in_stock    SMALLINT,
    units_on_order    SMALLINT,
    reorder_level     SMALLINT,
    discontinued      INTEGER                                              NOT NULL
);

CREATE OR REPLACE FUNCTION build_audit_products() RETURNS TRIGGER AS
$$
BEGIN
    IF tg_op = 'INSERT' THEN
        INSERT INTO products_audit
        SELECT 'I', SESSION_USER, NOW(), nt.*
        FROM new_table nt;
    ELSEIF tg_op = 'UPDATE' THEN
        INSERT INTO products_audit
        SELECT 'U', SESSION_USER, NOW(), nt.*
        FROM new_table nt;
    ELSEIF tg_op = 'DELETE' THEN
        INSERT INTO products_audit
        SELECT 'D', SESSION_USER, NOW(), ot.*
        FROM old_table ot;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS audit_products_insert ON products;
CREATE TRIGGER audit_products_insert
    AFTER INSERT
    ON products
    REFERENCING new TABLE AS new_table
    FOR EACH STATEMENT
EXECUTE PROCEDURE build_audit_products();

DROP TRIGGER IF EXISTS audit_products_update ON products;
CREATE TRIGGER audit_products_update
    AFTER UPDATE
    ON products
    REFERENCING new TABLE AS new_table
    FOR EACH STATEMENT
EXECUTE PROCEDURE build_audit_products();

DROP TRIGGER IF EXISTS audit_products_delete ON products;
CREATE TRIGGER audit_products_delete
    AFTER DELETE
    ON products
    REFERENCING old TABLE AS old_table
    FOR EACH STATEMENT
EXECUTE PROCEDURE build_audit_products();

SELECT *
FROM products
ORDER BY product_id DESC;

INSERT INTO products
VALUES (81, 'product_name', 1, 1, 1, 1, 1, 1, 1, 0);

SELECT *
FROM products_audit;

UPDATE products
SET unit_price = 50
WHERE product_id = 79;

SELECT *
FROM products_audit;

DELETE
FROM products
WHERE product_id = 80;

SELECT *
FROM products_audit;

-- 1. Автоматизировать логирование времени последнего изменения в таблице products. Добавить в products соответствующую
-- колонку и реализовать построчный триггер.

ALTER TABLE products
    ADD COLUMN last_updated TIMESTAMP;

CREATE OR REPLACE FUNCTION track_products_changes_function() RETURNS TRIGGER AS
$$
BEGIN
    new.last_updated = NOW();
    RETURN new;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS track_products_changes_trigger ON products;
CREATE TRIGGER track_products_changes_trigger
    BEFORE INSERT OR UPDATE
    ON products
    FOR EACH ROW
EXECUTE PROCEDURE track_products_changes_function();

SELECT last_updated, *
FROM products
WHERE product_id = 2;

ALTER TABLE products
    DISABLE TRIGGER audit_products_update;

UPDATE products
SET unit_price = 19.05
WHERE product_id = 2;

-- 2. Автоматизировать аудит операций в таблице order_details. Создайте отдельную таблицу для аудита, добавьте туда
-- колонки для хранения наименования операций, имени пользователя и временного штампа. Реализуйте триггеры на утверждения.

DROP TABLE IF EXISTS order_details_audit;
CREATE TABLE order_details_audit
(
    op           CHAR(1)   NOT NULL,
    user_changed TEXT      NOT NULL,
    time_stamp   TIMESTAMP NOT NULL,

    order_id     SMALLINT  NOT NULL,
    product_id   SMALLINT  NOT NULL,
    unit_price   REAL      NOT NULL,
    quantity     SMALLINT  NOT NULL,
    discount     REAL      NOT NULL
);

CREATE OR REPLACE FUNCTION build_audit_order_details() RETURNS TRIGGER AS
$$
BEGIN
    IF tg_op = 'INSERT' THEN
        INSERT INTO order_details_audit
        SELECT 'I', SESSION_USER, NOW(), nt.*
        FROM new_table nt;
    ELSEIF tg_op = 'UPDATE' THEN
        INSERT INTO order_details_audit
        SELECT 'U', SESSION_USER, NOW(), nt.*
        FROM new_table nt;
    ELSEIF tg_op = 'DELETE' THEN
        INSERT INTO order_details_audit
        SELECT 'D', SESSION_USER, NOW(), ot.*
        FROM old_table ot;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS insert_order_details_trigger ON order_details;
CREATE TRIGGER insert_order_details_trigger
    AFTER INSERT
    ON order_details
    REFERENCING new TABLE AS new_table
    FOR EACH STATEMENT
EXECUTE PROCEDURE build_audit_order_details();

DROP TRIGGER IF EXISTS update_order_details_trigger ON order_details;
CREATE TRIGGER update_order_details_trigger
    AFTER UPDATE
    ON order_details
    REFERENCING new TABLE AS new_table
    FOR EACH STATEMENT
EXECUTE PROCEDURE build_audit_order_details();

DROP TRIGGER IF EXISTS delete_order_details_trigger ON order_details;
CREATE TRIGGER delete_order_details_trigger
    AFTER DELETE
    ON order_details
    REFERENCING old TABLE AS old_table
    FOR EACH STATEMENT
EXECUTE PROCEDURE build_audit_order_details();

SELECT *
FROM order_details
ORDER BY order_id DESC;


ALTER TABLE order_details
    DROP CONSTRAINT fk_order_details_orders;
ALTER TABLE order_details
    DROP CONSTRAINT fk_order_details_products;



INSERT INTO order_details
VALUES (11077, 79, 13, 2, 0);

UPDATE order_details
set unit_price = 50 where order_id = 11077;

DELETE
FROM order_details
WHERE order_id = 11077;

SELECT *
FROM order_details_audit;
