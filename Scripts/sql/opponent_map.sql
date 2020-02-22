SELECT map, opponentrace, COUNT(map)
FROM replays
GROUP BY opponentrace, map
ORDER BY opponentrace, map;