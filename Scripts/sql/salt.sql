CREATE TABLE salttable AS
SELECT opponentrace AS saltyrace, COUNT(opponentrace) AS saltycount
FROM replays
WHERE instr(tags, 'salt') > 0
GROUP BY opponentrace;

SELECT saltyrace, saltycount * 1.0 / COUNT(opponentrace)
FROM salttable, replays
WHERE saltyrace = opponentrace
GROUP BY opponentrace;

DROP TABLE IF EXISTS salttable;