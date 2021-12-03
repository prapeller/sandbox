CREATE TABLE chess_game
(
    white_player TEXT,
    black_player TEXT,
    moves        TEXT[],
    final_state  TEXT[][]
);

INSERT INTO chess_game
VALUES ('Cauana',
        'Nakamura',
        '{"d4", "d5", "c4", "c6"}',
        '{{"Ra8", "Qe8", "x", "x", "x", "x", "x", "x"}, {"a7", "x", "x", "x", "x", "x", "x", "x"}, {"Kb5", "Bc5", "d5", "x", "x", "x", "x", "x"}}');

SELECT *
FROM chess_game;

INSERT INTO chess_game
VALUES ('Cauana',
        'Nakamura',
        ARRAY ['d4', 'd5', 'c4', 'c6'],
        ARRAY [
            ['Ra8', 'Qe8', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['a7', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['Kb5', 'Bc5', 'd5', 'x', 'x', 'x', 'x', 'x']
            ]);


SELECT *
FROM chess_game;

SELECT moves[2:4]
FROM chess_game;
SELECT moves[:4]
FROM chess_game;
SELECT moves[3:]
FROM chess_game;

SELECT ARRAY_DIMS(moves), ARRAY_LENGTH(moves, 1)
FROM chess_game;

SELECT ARRAY_DIMS(final_state), ARRAY_LENGTH(moves, 1)
FROM chess_game;

UPDATE chess_game
SET moves= ARRAY ['bla','bla','bla','bla','bla','bla','bla'];

SELECT *
FROM chess_game;

UPDATE chess_game
SET moves[4] = 'boom';

UPDATE chess_game
SET moves[5] = 'spam';

SELECT *
FROM chess_game;

SELECT *
FROM chess_game
WHERE 'boom' = ANY (moves);

-- operators
SELECT ARRAY [1, 2, 3] = ARRAY [1, 2, 3];
SELECT ARRAY [1, 2, 3] = ARRAY [1, 3, 2];
SELECT ARRAY [1, 3, 2] > ARRAY [1, 2, 3];
SELECT ARRAY [1, 2, 3] < ARRAY [1, 3, 3];

SELECT ARRAY [1, 2, 3, 4] @> ARRAY [1, 2];
SELECT ARRAY [1, 2, 3, 4] @> ARRAY [1, 6];

SELECT ARRAY [1, 2] <@ ARRAY [1, 2, 3, 4];
SELECT ARRAY [1, 5] <@ ARRAY [1, 2, 3, 4];

SELECT ARRAY [1, 5] && ARRAY [1, 2, 3, 4];
SELECT ARRAY [1] && ARRAY [1, 2, 3, 4];
SELECT ARRAY [5] && ARRAY [1, 2, 3, 4];

SELECT *
FROM chess_game
WHERE moves && ARRAY ['bla'];

-- variadic

CREATE OR REPLACE FUNCTION filter_even(VARIADIC numbers INT[]) RETURNS SETOF INT AS
$$
    -- DECLARE
--     counter INT;
BEGIN
    --     FOREACH counter IN ARRAY numbers
    FOR counter IN 1..ARRAY_UPPER(numbers, 1)
        LOOP
            CONTINUE WHEN counter % 2 != 0;
            RETURN NEXT counter;
        END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT *
FROM filter_even(1, 2, 3, 4, 5, 6);


-- homework
-- CREATE OR REPLACE FUNCTION get_avg_freight_by_countries(countries VARCHAR[]) returns float8 AS
CREATE OR REPLACE FUNCTION get_avg_freight_by_countries(VARIADIC countries TEXT[]) RETURNS float8 AS
$$
SELECT AVG(freight)
FROM orders
WHERE ship_country = ANY (countries);
$$
    LANGUAGE sql;

SELECT get_avg_freight_by_countries(VARIADIC ARRAY ['USA', 'UK']);
SELECT get_avg_freight_by_countries('USA', 'UK');


-- Написать функцию, которая фильтрует телефонные номера по коду оператора.
-- Принимает 3-х значный код мобильного оператора и список телефонных номеров в формате +1(234)5678901 (variadic)
-- Функция возвращает только те номера, код оператора которых соответствует значению соответствующего аргумента.
-- Проверить функцию передав следующие аргументы:
-- 903, +7(903)1901235, +7(926)8567589, +7(903)1532476
-- Попробовать передать аргументы с созданием массива и без.
-- Подсказка: чтобы передать массив в VARIADIC-аргумент, надо перед массивом прописать, собственно, ключевое слово variadic.

CREATE OR REPLACE FUNCTION filter_phones_by_code(code INT, VARIADIC phones TEXT[]) RETURNS SETOF TEXT AS
$$
DECLARE
    cur_phone TEXT;
BEGIN
    FOREACH cur_phone IN ARRAY phones
        LOOP
            RAISE NOTICE 'cur phone is %', cur_phone;
            CONTINUE WHEN cur_phone NOT LIKE '%(' || code::TEXT || ')%';
            RETURN NEXT cur_phone;
        END LOOP;
END;
$$
    LANGUAGE plpgsql;

SELECT *
FROM filter_phones_by_code(903, '+7(903)1901235', '+7(926)8567589', '+7(903)1532476')