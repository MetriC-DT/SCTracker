import sqlite3
import glob
import os
import functions
import matplotlib.pyplot as plt
import numpy as np

connection = functions.get_database_copy('winrate.py')
c = connection.cursor()
wins = dict(functions.execute_file('winrate.sql', c))
functions.remove_database_copy(connection, c, 'winrate.py')

connection = functions.get_database_copy('winrate.py')
c = connection.cursor()
totalraces = dict(functions.execute_file('races.sql', c))
functions.remove_database_copy(connection, c, 'winrate.py')

winrate_dict = dict()
for race in wins.keys():
    winrate_dict[race] = wins[race] / totalraces[race] * 100


plt.rcdefaults()
fig, ax = plt.subplots()

races = winrate_dict.keys()
y_pos = np.arange(len(races))
winrate = winrate_dict.values()

ax.barh(y_pos, winrate, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(races)
ax.set_xlabel('Winrate')
ax.set_title('My Winrate By Opponent Race')

plt.show()