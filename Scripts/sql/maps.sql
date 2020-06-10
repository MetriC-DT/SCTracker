SELECT map
FROM replays
WHERE map=="Eternal Empire LE"
OR map=="Ever Dream LE"
OR map=="Deathaura LE"
OR map=="Ice and Chrome LE"
OR map=="Pillars of Gold LE"
OR map=="Submarine LE"
OR map=="Golden Wall LE"
GROUP BY map
ORDER BY map;