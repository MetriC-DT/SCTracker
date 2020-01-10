import sqlite3
import glob
import os
import functions
import matplotlib.pyplot as plt
import numpy as np

connection = functions.get_database()
c = connection.cursor()

salty_players = dict(functions.execute_file('salt.sql', c))

plt.rcdefaults()
fig, ax = plt.subplots()

races = salty_players.keys()
y_pos = np.arange(len(races))
salt = salty_players.values()

ax.barh(y_pos, salt, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(races)
ax.set_xlabel('Percent of race salty')
ax.set_title('Salt By Race')

plt.show()