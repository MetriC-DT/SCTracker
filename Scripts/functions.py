import os
import glob
import sqlite3

def get_database():
    this_directory = os.path.dirname(os.path.abspath(__file__))
    replays_directory = os.path.abspath(os.path.join(this_directory, '..'))
    filepath = os.path.abspath(replays_directory + '/replays.db')
    connection = sqlite3.connect(filepath)
    return connection


def execute_file(filename, cursor):
    sql_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sql/')
    fd = open(sql_path + filename, 'r')
    sqlFile = fd.read()
    fd.close()
    commands = [item for item in sqlFile.split(';') if item != '']
    return_value = None

    for command in commands:
        cursor.execute(command)
        if('DROP TABLE' not in command.upper()):
            return_value = cursor.fetchall()

    return return_value
