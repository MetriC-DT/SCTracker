SELECT map, opponentrace, SUM(win)/COUNT(win)*100 AS winrate
FROM replays
WHERE (win=1.0 OR win=0.0) AND NOT instr(tags, "unranked") AND NOT instr(tags, "custom")
GROUP BY map, opponentrace
ORDER BY map, opponentrace;