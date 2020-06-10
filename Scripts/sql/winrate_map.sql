SELECT map, opponentrace, SUM(win)/COUNT(win)*100 AS winrate
FROM replays
WHERE (win=1.0 OR win=0.0) AND 
(map=="Eternal Empire LE"
OR map=="Ever Dream LE"
OR map=="Deathaura LE"
OR map=="Ice and Chrome LE"
OR map=="Pillars of Gold LE"
OR map=="Submarine LE"
OR map=="Golden Wall LE")
GROUP BY map, opponentrace
ORDER BY map, opponentrace;