import sqlite3

class database():
    filename = 'replays.db'
    replays_table = 'replays'
    build_order_table = 'builds'

    def __init__(self):
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()

    def get_data(self, string):
        self.cursor.execute(string)
        return self.cursor.fetchall()


    def add_replay_entry(self, values):
        print("adding replay entry")
        
        inserted_values = list()
        for key in values:
            if len(key) >= 5 and key[len(key) - len('input'):] == 'input':
                inserted_values.append(values[key])

        execute_string = 'INSERT INTO ' + self.replays_table + ' VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'
        self.cursor.execute(execute_string, inserted_values)
        self.commit()
    

    def add_build_entry(self, build):
        build[0] = int(build[0])
        self.cursor.execute('INSERT INTO ' + self.build_order_table + ' VALUES (?, ?, ?);', (build[0], build[1], build[2]))
        self.commit()
        print('added new build to table')

    def create_tables(self):
        execute_string = "CREATE TABLE IF NOT EXISTS " + self.replays_table + """
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
                win DOUBLE,
                gameplan INTEGER,
                openersuccess DOUBLE,
                buildorder TEXT,
                reaction TEXT,
                followup TEXT,
                tags TEXT,
                length INTEGER,
                notes TEXT,
                path TEXT
            );"""
        self.cursor.execute(execute_string)

        execute_string = "CREATE TABLE IF NOT EXISTS " + self.build_order_table + """
            (
                number INTEGER,
                opponent TEXT,
                description TEXT
            );"""
        self.cursor.execute(execute_string)
        self.connection.commit()