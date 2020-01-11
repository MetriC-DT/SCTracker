SELECT opponentrace, COUNT(opponentrace)
FROM replays
WHERE opponentrace LIKE "%P%" OR opponentrace LIKE "%Z%" OR opponentrace LIKE "%T%"
GROUP BY opponentrace;