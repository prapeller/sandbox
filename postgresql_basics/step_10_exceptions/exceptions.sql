CREATE OR REPLACE FUNCTION get_season(month_number INT) RETURNS TEXT AS
$$
DECLARE
    season VARCHAR(10);
BEGIN
    IF month_number NOT BETWEEN 1 AND 12 THEN
        RAISE EXCEPTION 'Invalid month_numer. You passed:(%)', month_number USING HINT = 'Allowed from 1 up to 12', ERRCODE = 12992;
    END IF;
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
SELECT get_season(15);


CREATE OR REPLACE FUNCTION get_season_caller(month_number INT) RETURNS TEXT AS
$$
DECLARE
    err_ctx     TEXT;
    err_msg     TEXT;
    err_details TEXT;
    err_code    TEXT;
BEGIN
    RETURN get_season(month_number);
EXCEPTION
    WHEN SQLSTATE '12992' THEN
        GET STACKED DIAGNOSTICS
            err_ctx = PG_EXCEPTION_CONTEXT,
            err_msg = MESSAGE_TEXT,
            err_details = PG_EXCEPTION_DETAIL,
            err_code = RETURNED_SQLSTATE;
        RAISE INFO 'my custom handler: ctx: %, msg: %, details: %, code: %', err_ctx, err_msg, err_details, err_code;
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;

SELECT get_season_caller(15);


CREATE OR REPLACE FUNCTION get_season_caller2(month_number INT) RETURNS TEXT AS
$$
DECLARE
    err_ctx     TEXT;
    err_msg     TEXT;
    err_details TEXT;
    err_code    TEXT;
BEGIN
    RETURN get_season(month_number);
EXCEPTION
    WHEN SQLSTATE '12993' THEN
        GET STACKED DIAGNOSTICS
            err_ctx = PG_EXCEPTION_CONTEXT,
            err_msg = MESSAGE_TEXT,
            err_details = PG_EXCEPTION_DETAIL,
            err_code = RETURNED_SQLSTATE;
        RAISE INFO 'my custom handler: ctx: %, msg: %, details: %, code: %', err_ctx, err_msg, err_details, err_code;
        RETURN NULL;
    WHEN OTHERS THEN
        RAISE INFO 'others';
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;

SELECT get_season_caller2(15);

-- homework
-- Имеется следующая функция, которую мы написали в разделе, посвящённом, собственно, функциям:
--
-- create or replace function should_increase_salary(
-- 	cur_salary numeric,
-- 	max_salary numeric DEFAULT 80,
-- 	min_salary numeric DEFAULT 30,
-- 	increase_rate numeric DEFAULT 0.2
-- 	) returns bool AS $$
-- declare
-- 	new_salary numeric;
-- begin
-- 	if cur_salary >= max_salary or cur_salary >= min_salary then
-- 		return false;
-- 	end if;
--
-- 	if cur_salary < min_salary then
-- 		new_salary = cur_salary + (cur_salary * increase_rate);
-- 	end if;
--
-- 	if new_salary > max_salary then
-- 		return false;
-- 	else
-- 		return true;
-- 	end if;
-- end;
-- $$ language plpgsql;
-- Задание:
--
-- Модифицировать функцию should_increase_salary разработанную в секции по функциям таким образом,
-- чтобы запретить (выбрасывая исключения) передачу аргументов так, что:
-- минимальный уровень з/п превышает максимальный
-- ни минимальный, ни максимальный уровень з/п не могут быть меньше нуля
-- коэффициент повышения зарплаты не может быть ниже 5%
--
-- Протестировать реализацию, передавая следующие значения аргументов
-- (с - уровень "проверяемой" зарплаты, r - коэффициент повышения зарплаты):
-- c = 79, max = 10, min = 80, r = 0.2
-- c = 79, max = 10, min = -1, r = 0.2
-- c = 79, max = 10, min = 10, r = 0.04

CREATE OR REPLACE FUNCTION should_increase(
    cur_sal NUMERIC,
    max_sal NUMERIC DEFAULT 80,
    min_sal NUMERIC DEFAULT 30,
    raise_rate FLOAT DEFAULT 1.2
)
    RETURNS bool AS
$$
BEGIN
    IF min_sal > max_sal THEN
        RAISE EXCEPTION 'Invalid salaries. You passed:(min_sal: %, max_sal: %)', min_sal, max_sal USING HINT = 'min_sal cant be > max_sal', ERRCODE = 12300;
    ELSEIF min_sal < 0 OR max_sal < 0 THEN
        RAISE EXCEPTION 'Invalid salaries. You passed:(min_sal: %, max_sal: %)', min_sal, max_sal USING HINT = 'min_sal or max_sal cant be < 0>', ERRCODE = 12301;
    ELSEIF raise_rate < 1.05 THEN
        RAISE EXCEPTION 'Invalid raise_rate. You passed:(raise_rate: %)', raise_rate USING HINT = 'raise_rate cant be < 1.05>', ERRCODE = 12302;
    END IF;
    IF cur_sal >= min_sal THEN
        RETURN FALSE;
    ELSEIF cur_sal < min_sal THEN
        cur_sal = cur_sal * raise_rate;
        IF cur_sal > max_sal THEN
            RETURN FALSE;
        ELSE
            RETURN TRUE;
        END IF;
    END IF;
END;
$$
    LANGUAGE plpgsql;


SELECT should_increase(79, 10, 80, 1.2);
SELECT should_increase(79, 10, -1, 1.2);
SELECT should_increase(79, 10, 10, 1.04);
