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

ax.barh(y_pos, winrate, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(races)
ax.set_xlabel('Winrate')
ax.set_title('My Winrate By Opponent Race')

for i, v in enumerate(winrate):
    ax.text(v + 1, i, str(v) + '%', va='center')

plt.show()