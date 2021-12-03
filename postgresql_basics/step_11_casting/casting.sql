CREATE OR REPLACE FUNCTION type_testing(money_val float8) RETURNS VOID AS
$$
BEGIN
    RAISE NOTICE 'ran %', money_val;
END;
$$
    LANGUAGE plpgsql;

SELECT type_testing(0.5);
SELECT type_testing(0.5::float8);
SELECT type_testing(0.5::float4);
SELECT type_testing(1);


CREATE OR REPLACE FUNCTION type_testing2(money_val INT) RETURNS VOID AS
$$
BEGIN
    RAISE NOTICE 'ran %', money_val;
END;
$$
    LANGUAGE plpgsql;

SELECT type_testing2(1);
SELECT type_testing2(0.5);
SELECT type_testing(0.5::INT);
SELECT type_testing(0.3::INT);
SELECT type_testing(CAST(0.4 AS INT));

SELECT type_testing2('1.5');
SELECT type_testing2('1.5'::INT);
SELECT type_testing2('1.5'::NUMERIC::INT);

SELECT type_testing2('1'::INT);

-- implicit casting
SELECT 50! AS big_factorial;
-- explicit casting
SELECT CAST(50 AS BIGINT)! AS big_factorial;

SELECT 'abc' || 1;
SELECT ' 10 ' = 10;