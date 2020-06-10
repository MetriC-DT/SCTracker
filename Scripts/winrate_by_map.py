import functions
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

connection = functions.get_database_copy('winrate_by_map.py')
cursor = connection.cursor()

result = functions.execute_file('winrate_map.sql', cursor)
functions.remove_database_copy(connection, cursor, 'winrate_by_map.py')

maps_list = [row[0] for row in result]

# removes duplicates
for i in range(len(maps_list) - 1, 0, -1):
    if maps_list.count(maps_list[i]) > 1:
        maps_list.pop(i)

races = ['P', 'T', 'Z']

protoss_dict = dict()
terran_dict = dict()
zerg_dict = dict()

for mapname in maps_list:
	protoss_dict[mapname] = [entry[2] for entry in result if entry[0] == mapname and entry[1] == 'P']
	terran_dict[mapname] = [entry[2] for entry in result if entry[0] == mapname and entry[1] == 'T']
	zerg_dict[mapname] = [entry[2] for entry in result if entry[0] == mapname and entry[1] == 'Z']

protoss_data = list()
terran_data = list()
zerg_data = list()

for mapname in maps_list:
	protoss_data.append(protoss_dict[mapname][0] if len(protoss_dict[mapname]) != 0 else None)
	terran_data.append(terran_dict[mapname][0] if len(terran_dict[mapname]) != 0 else None)
	zerg_data.append(zerg_dict[mapname][0] if len(zerg_dict[mapname]) != 0 else None)

fig = plt.figure()
ax = fig.add_subplot()
width = 0.25
x = np.arange(len(maps_list))

protoss_bar = ax.bar(x - width, [(value or 0) for value in protoss_data], width, label='Protoss', color='tab:blue')
terran_bar = ax.bar(x, [(value or 0) for value in terran_data], width, label='Terran', color='tab:red')
zerg_bar = ax.bar(x + width, [(value or 0) for value in zerg_data], width, label='Zerg', color='tab:purple')

ax.set_ylabel('Winrate %')
ax.set_title('Winrate by Map')
ax.set_xticks(x)
ax.set_xticklabels(maps_list)
ax.legend()

functions.autolabel(ax, protoss_bar, [str(value)[:5] if value is not None else 'N/A' for value in protoss_data])
functions.autolabel(ax, terran_bar, [str(value)[:5] if value is not None else 'N/A' for value in terran_data])
functions.autolabel(ax, zerg_bar, [str(value)[:5] if value is not None else 'N/A' for value in zerg_data])

plt.tight_layout()
fig.canvas.manager.full_screen_toggle()
plt.show()