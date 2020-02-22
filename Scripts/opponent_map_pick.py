import sqlite3
import glob
import os
import functions
import matplotlib.pyplot as plt
import numpy as np

connection = functions.get_database_copy('opponent_map.py')
c = connection.cursor()

result = functions.execute_file('opponent_map.sql', c)
maps = functions.execute_file('maps.sql', c)
maps_list = [row[0] for row in maps]

protoss_data = list()
terran_data = list()
zerg_data = list()

races_dict = {
    'P': protoss_data,
    'T': terran_data,
    'Z': zerg_data
}


races_dict['P'] = [(data[0], data[2]) for data in result if data[1] == 'P']
races_dict['T'] = [(data[0], data[2]) for data in result if data[1] == 'T']
races_dict['Z'] = [(data[0], data[2]) for data in result if data[1] == 'Z']

for race in races_dict:
    for i in range(len(maps_list)):
        rowdata = races_dict[race]
        try:
            mapName = rowdata[i][0]
            mapCount = rowdata[i][1]

            if mapName != maps_list[i]:
                rowdata.insert(i,  0)
            else:
                rowdata[i] = mapCount
        except:
            rowdata.append(0)

protoss_data = races_dict['P']
terran_data = races_dict['T']
zerg_data = races_dict['Z']


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