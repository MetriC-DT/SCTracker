import os
import glob
import sqlite3
import shutil
import time

def get_database_copy(accessorfile):
    this_directory = os.path.dirname(os.path.abspath(__file__))
    replays_directory = os.path.abspath(os.path.join(this_directory, '..'))
    replays_filepath = os.path.abspath(replays_directory + '/replays.db')
    copy_filepath = os.path.join(this_directory, accessorfile + '.db')
    copy = shutil.copyfile(replays_filepath, copy_filepath)
    connection = sqlite3.connect(copy_filepath)
    return connection


def execute_file(sqlfilename, cursor):
    sql_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sql/')
    fd = open(sql_path + sqlfilename, 'r')
    sqlFile = fd.read()
    fd.close()
    commands = [item for item in sqlFile.split(';') if item != '']
    return_value = None

    for command in commands:
        try:
            cursor.execute(command)
            result = cursor.fetchall()
            if(result):
                return_value = result
        except sqlite3.OperationalError as e:
            print(e)

    return return_value


def remove_database_copy(connection, cursor, filename):
    this_directory = os.path.dirname(os.path.abspath(__file__))
    cursor.close()
    connection.close()
    os.remove(os.path.join(this_directory, filename + '.db'))


def autolabel(ax, rects, labels):
    if len(rects) != len(labels):
        return None
    else:
        for i in range(len(rects)):
            height = rects[i].get_height()
            ax.text(rects[i].get_x() + rects[i].get_width()/2, height, labels[i], ha='center', va='bottom')