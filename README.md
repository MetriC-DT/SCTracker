# SCTracker
Personal Replay tracker for SC2, inspired by Quasarprintf's spreadsheet

## Tables
|table name|table description|
|----------|-----------------|
|replays   |contains replay data|
|builds    | contains your build info|

## Columns for replays Table
| Column Name | Column description | Data Type|
|-------------|--------------------|----------|
| gamenumber | Game Number | INTEGER
| datetime | DateTime | DATETIME
| playername | Player Name | TEXT
| playermmr | Player MMR | INTEGER
| playerleague | Player League | TEXT
| playerrace | Player Race | TEXT
| playerclan | Player Clan | TEXT
| opponentname | Opponent Name | TEXT
| opponentmmr | Opponent MMR | INTEGER
| opponentleague | Opponent League | TEXT
| opponentrace | Opponent Race | TEXT
| opponentclan | Opponent Clan | TEXT
| map | Map | TEXT
| win | 0=loss, 1=win, 0.5=tie | DOUBLE
| gameplan | ID of Game Plan | INTEGER
| openersuccess | Opener successful? | DOUBLE
| buildorder | Opponent Build Order | TEXT
| reaction | Opponent Reaction | TEXT
| followup | Opponent followup | TEXT
| tags | tags | TEXT
| length | game length | INTEGER
| notes | Notes | TEXT
| path | path to replay | TEXT

## Columns for builds
| Column Name | Column Description | Data Type |
|-------------|--------------------|-----------|
|number| id of the build | INTEGER|
|opponent| opponent race | TEXT|
|description| description of the build | TEXT|