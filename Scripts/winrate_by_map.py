import functions
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

connection = functions.get_database_copy('winrate_by_map.py')
cursor = connection.cursor()

result = functions.execute_file('winrate_map.sql', cursor)
functions.remove_database_copy(connection, cursor, 'winrate_by_map.py')

maps_list = [row[0] for row in result]

for i in range(len(maps_list) - 1, 0, -1):
    if maps_list.count(maps_list[i]) > 1:
        maps_list.pop(i)

races = ['P', 'T', 'Z']

bar_data = [row[1:] for row in result]

# gets the data to be groups of three, so it matches the PTZ format
race_index = 0
for i in range(len(bar_data)):
    if bar_data[i][0] != races[race_index]:
        bar_data.insert(i, (races[race_index], None))
    race_index = (race_index + 1) % len(races)

protoss_data = list()
terran_data = list()
zerg_data = list()
for data in bar_data:
    if data[0] == 'P':
        protoss_data.append(data[1])
    elif data[0] == 'T':
        terran_data.append(data[1])
    elif data[0] == 'Z':
        zerg_data.append(data[1])


fig = plt.figure()
ax = fig.add_subplot()
width = 0.25
x = np.arange(len(maps_list))

protoss_bar = ax.bar(x - width, [(value or 0) for value in protoss_data], width, label='Protoss', color='tab:blue')
terran_bar = ax.bar(x, [(value or 0) for value in terran_data], width, label='Terran', color='tab:red')
zerg_bar = ax.bar(x + width, [(value or 0) for value in zerg_data], width, label='Zerg', color='tab:purple')

ax.set_ylabel('My Winrate')
ax.set_title('Winrate by Map')
ax.set_xticks(x)
ax.set_xticklabels(maps_list)
ax.legend()

functions.autolabel(ax, protoss_bar, [str(value)[:5] if value is not None else '?' for value in protoss_data])
functions.autolabel(ax, terran_bar, [str(value)[:5] if value is not None else '?' for value in terran_data])
functions.autolabel(ax, zerg_bar, [str(value)[:5] if value is not None else '?' for value in zerg_data])

plt.tight_layout()
fig.canvas.manager.full_screen_toggle()
plt.show()