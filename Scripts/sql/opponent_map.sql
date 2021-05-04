SELECT map, opponentrace, COUNT(map)
FROM replays
WHERE map=="2000 Atmospheres LE"
OR map=="Beckett Industries LE"
OR map=="Blackburn LE"
OR map=="Jagannatha LE"
OR map=="Lightshade LE LE"
OR map=="Oxide LE"
OR map=="Romanticide LE"
GROUP BY opponentrace, map
ORDER BY opponentrace, map;