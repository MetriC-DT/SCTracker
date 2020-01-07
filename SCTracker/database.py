import sqlite3

class database():
    filename = 'replays.db'
    table = 'replays'

    def __init__(self):
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.create_table()

    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()

    def execute(self, string):
        self.cursor.execute(string)
        return self.cursor.fetchall()

    def create_table(self):
        execute_string = "CREATE TABLE IF NOT EXISTS " + self.table + """
            (
                gamenumber INTEGER,
                datetime DATETIME,
                playername TEXT,
                playermmr INTEGER,
                playerleague TEXT,
                playerrace TEXT,
                playerclan TEXT,
                opponentname TEXT,
                opponentmmr INTEGER,
                opponentleague TEXT,
                opponentrace TEXT,
                opponentclan TEXT,
                map TEXT,
                win INTEGER,
                openersuccess INTEGER,
                gameplan INTEGER,
                buildorder TEXT,
                reaction TEXT,
                followup TEXT,
                tags TEXT,
                length INTEGER,
                notes TEXT,
                path TEXT
            )"""
        
        self.cursor.execute(execute_string)
        self.connection.commit()