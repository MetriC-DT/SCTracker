SELECT map, opponentrace, SUM(win)/COUNT(win)*100 AS winrate
FROM replays
WHERE (win=1.0 OR win=0.0) AND 
(map=="Eternal Empire LE"
OR map=="Ever Dream LE"
OR map=="Simulacrum LE"
OR map=="Nightshade LE"
OR map=="Purity and Industry LE"
OR map=="Zen LE"
OR map=="Golden Wall LE")
GROUP BY map, opponentrace
ORDER BY map, opponentrace;