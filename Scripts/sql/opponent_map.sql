SELECT map, opponentrace, COUNT(map)
FROM replays
WHERE map=="Eternal Empire LE"
OR map=="Ever Dream LE"
OR map=="Simulacrum LE"
OR map=="Nightshade LE"
OR map=="Purity and Industry LE"
OR map=="Zen LE"
OR map=="Golden Wall LE"
GROUP BY opponentrace, map
ORDER BY opponentrace, map;