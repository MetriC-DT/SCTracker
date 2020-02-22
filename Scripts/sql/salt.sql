CREATE TABLE saltyterran AS
SELECT replays.opponentrace AS saltyterran
FROM replays
WHERE instr(opponentrace, 'T') > 0 AND instr(tags, 'salt') > 0;

CREATE TABLE saltyprotoss AS
SELECT replays.opponentrace AS saltyprotoss
FROM replays
WHERE instr(opponentrace, 'P') > 0 AND instr(tags, 'salt') > 0;

CREATE TABLE saltyzerg AS
SELECT replays.opponentrace as saltyzerg
FROM replays
WHERE instr(opponentrace, 'Z') > 0 AND instr(tags, 'salt') > 0;

CREATE TABLE salttable (
    saltyrace TEXT,
    saltycount INTEGER
);

INSERT INTO salttable(saltyrace, saltycount)
SELECT 'Z', COUNT(saltyzerg)
FROM saltyzerg;

INSERT INTO salttable(saltyrace, saltycount)
SELECT 'T', COUNT(saltyterran)
FROM saltyterran;

INSERT INTO salttable(saltyrace, saltycount)
SELECT 'P', COUNT(saltyprotoss)
FROM saltyprotoss;

SELECT saltyrace, saltycount * 100.0 / COUNT(opponentrace)
FROM salttable, replays
WHERE saltyrace = opponentrace
GROUP BY opponentrace;