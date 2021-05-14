SELECT map, opponentrace, SUM(win)/COUNT(win)*100 AS winrate
FROM replays
WHERE (win=1.0 OR win=0.0) AND 
(map=="2000 Atmospheres LE"
OR map=="Beckett Industries LE"
OR map=="Blackburn LE"
OR map=="Jagannatha LE"
OR map=="Lightshade LE"
OR map=="Oxide LE"
OR map=="Romanticide LE")
GROUP BY map, opponentrace
ORDER BY map, opponentrace;