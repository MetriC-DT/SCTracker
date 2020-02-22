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

plt.rcdefaults()
fig, ax = plt.subplots()

races = wins.keys()
y_pos = np.arange(len(races))
winrate = wins.values()

bars = ax.bar(y_pos, winrate, align='center')
ax.set_xticks(y_pos)
ax.set_xticklabels(races)
ax.set_ylabel('Winrate')
ax.set_title('My Winrate By Opponent Race')

functions.autolabel(ax, bars, [str(val)[:5] + '%' for val in winrate])

plt.show()