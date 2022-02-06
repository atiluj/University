import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import pandas as pd
import numpy as np

zachorowania = pd.read_csv('COVID.csv', sep=';', usecols=['data', 'miesiac', 'zachorowania'])
zachorowania_lato = zachorowania.loc[(5 <= zachorowania['miesiac']) & (zachorowania['miesiac'] < 9)]
zachorowania_jesien = zachorowania.loc[(9 <= zachorowania['miesiac']) & (zachorowania['miesiac'] < 12)]


temperatura = pd.read_csv('temperatury.csv', sep=';', usecols=['data', 'miesiac', 'temperatura'])

for i in range(len(temperatura)):
    temperatura['temperatura'][i] = float(temperatura['temperatura'][i])

temperatura_lato = temperatura.loc[(5 <= temperatura['miesiac']) & (temperatura['miesiac'] < 9)]
temperatura_jesien = temperatura.loc[(9 <= temperatura['miesiac']) & (temperatura['miesiac'] < 12)]



fig, (ax1, ax3) = plt.subplots(2)
x_ticks = np.arange(0, len(zachorowania_lato['data']), 30)
plt.xticks(x_ticks)
ax1.plot(zachorowania_lato['data'], zachorowania_lato['zachorowania'], color='goldenrod')
ax2 = ax1.twinx()
ax2.plot(temperatura_lato['data'], temperatura_lato['temperatura'], color='darkgreen')
patch_1 = mpatches.Patch(color='goldenrod', label='liczba zachorowan')
patch_2 = mpatches.Patch(color='darkgreen', label='temperatura')
plt.title('ZACHOROWANIA LATEM')

x_ticks = np.arange(0, len(zachorowania_lato['data']), 30)
plt.xticks(x_ticks)
ax3.plot(zachorowania_jesien['data'], zachorowania_jesien['zachorowania'], color='goldenrod')
ax4 = ax3.twinx()
ax4.plot(temperatura_jesien['data'], temperatura_jesien['temperatura'], color='darkgreen')
ax3.legend(handles=[patch_1, patch_2],
           loc='upper center', bbox_to_anchor=(0.45, -0.3), ncol=2)
plt.title('ZACHOROWANIA JESIENIA')
fig.tight_layout(pad=3.0)
plt.show()

