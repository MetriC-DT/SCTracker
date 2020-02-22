import sqlite3
import glob
import os
import functions
import matplotlib.pyplot as plt
import numpy as np

connection = functions.get_database_copy('salt_by_race.py')
c = connection.cursor()

salty_players = dict(functions.execute_file('salt.sql', c))
functions.remove_database_copy(connection, c, 'salt_by_race.py')

fig, ax = plt.subplots()
plt.rcdefaults()

races = salty_players.keys()
y_pos = np.arange(len(races))
salt = list(salty_players.values())

bars = ax.bar(y_pos, salt, align='center')
ax.set_xticks(y_pos)
ax.set_xticklabels(races)
ax.set_ylabel('Percent of race salty')
ax.set_title('Salt By Race')

functions.autolabel(ax, bars, [str(val)[:5] + '%' for val in salt])

plt.show()