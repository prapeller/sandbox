-- psql -U user_name

-- \c db_name -- connect db_name
-- \l -- list db_names
-- \dn -- list of schemas
-- \dt -- all tables in current db
-- \d table_name -- table description
-- \db -- all db views
-- \df -- all db functions
-- \du -- all roles in cluster instance

-- \g -- repeat recent command
-- \i file_name -- lunch script file_name.sql
-- \? -- list of psql commands
-- \q -- exit from psql

-- kaggle.com/datasets/
DROP TABLE IF EXISTS reddit_vm;
CREATE TABLE reddit_vm
(
    title     VARCHAR,
    score     INT,
    id        VARCHAR,
    url       VARCHAR,
    comms_num INT,
    created   NUMERIC,
    body      TEXT,
    timestamp TIMESTAMP
);

\copy reddit_vm from 'C:\Users\prape\pycharm\udemy\postgres_sql\step_16_psql_import_from_csv\reddit_vm.csv' delimiter ',' csv header