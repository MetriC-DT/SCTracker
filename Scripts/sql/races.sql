SELECT opponentrace, COUNT(opponentrace)
FROM replays
GROUP BY opponentrace;