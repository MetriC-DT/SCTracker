SELECT opponentrace, COUNT(win)
FROM replays
WHERE win=1.0 AND (opponentrace LIKE "%P%" OR opponentrace LIKE "%Z%" OR opponentrace LIKE "%T%")
GROUP BY opponentrace;