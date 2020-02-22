SELECT opponentrace, SUM(win)/COUNT(win) * 100
FROM replays
WHERE win=1.0 OR win=0.0
GROUP BY opponentrace;