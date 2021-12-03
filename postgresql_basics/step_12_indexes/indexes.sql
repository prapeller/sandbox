SELECT amname
FROM pg_am;

-- btree - O(logN)

-- hash - O(1)

-- gist - generalized search tree
-- gin - generalized inversive
-- spgist - gist with binary space separation

-- brin - block/diapasonsn

-- heap


-- EXPLAIN ...query...

-- EXPLAIN ANALYZE ...query...

DROP TABLE perf_test;
CREATE TABLE perf_test
(
    id         INT,
    reason     TEXT COLLATE "C",
    annotation TEXT COLLATE "C"
);

INSERT INTO perf_test(id, reason, annotation)
SELECT s.id, MD5(RANDOM()::TEXT), NULL
FROM GENERATE_SERIES(1, 10000000) AS s(id)
ORDER BY RANDOM();

UPDATE perf_test
SET annotation = UPPER(MD5(RANDOM()::TEXT));


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

SELECT *
FROM perf_test
LIMIT 10;

SELECT *
FROM perf_test
WHERE id = 3700000;

EXPLAIN
SELECT *
FROM perf_test
WHERE id = 3700000;
-- Gather  (cost=1000.00..259582.55 rows=1 width=70)
--   Workers Planned: 2
--   ->  Parallel Seq Scan  (SEQUENTIAL SCAN) on perf_test  (cost=0.00..258582.45 rows=1 width=70)
--         Filter: (id = 3700000)

CREATE INDEX idx_perf_test_id ON perf_test (id);

EXPLAIN
SELECT *
FROM perf_test
WHERE id = 3700000;
-- Index Scan (BITMAP INDEX SCAN) using idx_perf_test_id on perf_test  (cost=0.43..8.45 rows=1 width=70)
--   Index Cond: (id = 3700000)


EXPLAIN
SELECT *
FROM perf_test
WHERE reason LIKE 'bc%'
  AND annotation LIKE 'AB%';
-- Gather  (cost=1000.00..270292.00 rows=10 width=70)
--   Workers Planned: 2
--   ->  Parallel Seq Scan on perf_test  (cost=0.00..269291.00 rows=4 width=70)
--         Filter: ((reason ~~ 'bc%'::text) AND (annotation ~~ 'AB%'::text))

EXPLAIN ANALYZE
SELECT *
FROM perf_test
WHERE reason LIKE 'bc%'
  AND annotation LIKE 'AB%';
-- Gather  (cost=1000.00..270292.00 rows=10 width=70) (actual time=24.254..12493.710 rows=143 loops=1)
--   Workers Planned: 2
--   Workers Launched: 2
--   ->  Parallel Seq Scan on perf_test  (cost=0.00..269291.00 rows=4 width=70) (actual time=38.575..12336.441 rows=48 loops=3)
--         Filter: ((reason ~~ 'bc%'::text) AND (annotation ~~ 'AB%'::text))
--         Rows Removed by Filter: 3333286
-- Planning Time: 0.157 ms
-- Execution Time: 12493.849 ms

-- ANALYZE perf_test; makes some improvement on performance

CREATE INDEX idx_perf_test_reason_annotation ON perf_test (reason, annotation);

EXPLAIN
SELECT *
FROM perf_test
WHERE reason LIKE 'bc%'
  AND annotation LIKE 'AB%';
-- Index Scan using idx_perf_test_reason_annotation on perf_test  (cost=0.56..2066.11 rows=10 width=70)
--   Index Cond: ((reason >= 'bc'::text) AND (reason < 'bd'::text) AND (annotation >= 'AB'::text) AND (annotation < 'AC'::text))
--   Filter: ((reason ~~ 'bc%'::text) AND (annotation ~~ 'AB%'::text))

EXPLAIN
SELECT *
FROM perf_test
WHERE reason LIKE 'bc%';
-- Bitmap Heap Scan on perf_test  (cost=1805.19..86321.68 rows=101010 width=70)
--   Filter: (reason ~~ 'bc%'::text)
--   ->  Bitmap Index Scan on idx_perf_test_reason_annotation  (cost=0.00..1779.94 rows=31538 width=0)
--         Index Cond: ((reason >= 'bc'::text) AND (reason < 'bd'::text))

EXPLAIN
SELECT *
FROM perf_test
WHERE annotation LIKE 'AB%';
-- Gather  (cost=1000.00..259974.33 rows=1000 width=70)
--   Workers Planned: 2
--   ->  Parallel Seq Scan on perf_test  (cost=0.00..258874.33 rows=417 width=70)
--         Filter: (annotation ~~ 'AB%'::text)


CREATE INDEX idx_perf_test_test_annotation ON perf_test (annotation);


EXPLAIN
SELECT *
FROM perf_test
WHERE annotation LIKE 'AB%';
-- Bitmap Heap Scan on perf_test  (cost=393.99..33552.67 rows=1000 width=70)
--   Filter: (annotation ~~ 'AB%'::text)
--   ->  Bitmap Index Scan on idx_perf_test_test_annotation  (cost=0.00..393.74 rows=10118 width=0)
--         Index Cond: ((annotation >= 'AB'::text) AND (annotation < 'AC'::text))

EXPLAIN
SELECT *
FROM perf_test
WHERE LOWER(annotation) LIKE 'ab%';
-- Gather  (cost=1000.00..256695.09 rows=36225 width=70)
--   Workers Planned: 2
--   ->  Parallel Seq Scan on perf_test  (cost=0.00..252072.59 rows=15094 width=70)
--         Filter: (lower(annotation) ~~ 'ab%'::text)

CREATE INDEX idx_per_test_annotaion_lower ON perf_test (LOWER(annotation));

EXPLAIN
SELECT *
FROM perf_test
WHERE LOWER(annotation) LIKE 'ab%';
-- Bitmap Heap Scan on perf_test  (cost=1957.06..118984.28 rows=50000 width=70)
--   Filter: (lower(annotation) ~~ 'ab%'::text)
--   ->  Bitmap Index Scan on idx_per_test_annotaion_lower  (cost=0.00..1944.56 rows=50000 width=0)
--         Index Cond: ((lower(annotation) >= 'ab'::text) AND (lower(annotation) < 'ac'::text))


EXPLAIN
SELECT *
FROM perf_test
WHERE reason LIKE '%bc%';
-- Seq Scan on perf_test  (cost=0.00..331791.00 rows=1515152 width=70)
--   Filter: (reason ~~ '%bc%'::text)

CREATE EXTENSION pg_trgm;

CREATE INDEX trgm_idx_per_test_reason ON perf_test USING gin (reason gin_trgm_ops);

EXPLAIN ANALYZE
SELECT *
FROM perf_test
WHERE reason LIKE '%bc%';
-- Seq Scan on perf_test  (cost=0.00..331791.00 rows=1515152 width=70) (actual time=0.404..6538.038 rows=1146826 loops=1)
--   Filter: (reason ~~ '%bc%'::text)
--   Rows Removed by Filter: 8853174
-- Planning Time: 4.869 ms
-- Execution Time: 6581.152 ms

EXPLAIN ANALYZE
SELECT *
FROM perf_test
WHERE reason LIKE '%bca%';
-- Gather  (cost=1946.83..215453.45 rows=101010 width=70) (actual time=78.632..4503.868 rows=73294 loops=1)
--   Workers Planned: 2
--   Workers Launched: 2
--   ->  Parallel Bitmap Heap Scan on perf_test  (cost=946.83..204352.45 rows=42088 width=70) (actual time=23.789..4348.113 rows=24431 loops=3)
--         Recheck Cond: (reason ~~ '%bca%'::text)
--         Heap Blocks: exact=21240
--         ->  Bitmap Index Scan on trgm_idx_per_test_reason  (cost=0.00..921.58 rows=101010 width=0) (actual time=49.230..49.230 rows=73294 loops=1)
--               Index Cond: (reason ~~ '%bca%'::text)
-- Planning Time: 1.862 ms
-- Execution Time: 4514.564 ms