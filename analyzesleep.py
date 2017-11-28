#!/usr/bin/env python3
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframes = [ pd.read_csv(fname, delim_whitespace=True, header=None, comment='#',
                           names=['datetime','state'], index_col=0, parse_dates=True)
               for fname in glob.glob('log.sleep.*') ]
df = pd.concat(dataframes)

# for figuring out time periods
df['t0'] = df.index.copy()
df['t0'] = df['t0'].shift(1)
df['deltaT'] = df.index - df['t0']
df['deltaT'] = df['deltaT'].dt.total_seconds()

# for figuring out on/off state deltas
df['statediff'] = df['state'].diff()

#print(df.head())
#print('...')
#print(df.tail())

fig,ax = plt.subplots(nrows=3)
df['state'].plot(ax=ax[0])
#df['deltaT'].loc[(df['statediff']==0) & (df['state']==1)].plot(ax=ax[1])
#df['deltaT'].loc[(df['statediff']==0) & (df['state']==0)].plot(ax=ax[2])

nstdev = 1.0

irreg = df['deltaT'].loc[(df['statediff']==0) & (df['state']==1)]
#irreg.plot(color='k',linestyle='',marker='o',ax=ax[1])
irreg_clip = irreg[np.abs(irreg-irreg.mean()) <= (nstdev*irreg.std())]
irreg_clip.plot(color='k',linestyle='',marker='o',ax=ax[1])
ax[1].axhline(irreg_clip.mean(),color='k',ls='--')
irreg_clip = irreg[np.abs(irreg-irreg.mean()) > (nstdev*irreg.std())]
irreg_clip.plot(color='0.8',linestyle='',marker='o',ax=ax[1])

normal = df['deltaT'].loc[(df['statediff']==0) & (df['state']==0)]
normal_clip = normal[np.abs(normal-normal.mean()) <= (nstdev*normal.std())]
normal_clip.plot(color='k',linestyle='',marker='o',ax=ax[2])
ax[2].axhline(normal_clip.mean(),color='k',ls='--')

ax[0].set_xticks([])
ax[1].set_xticks([])
ax[0].set_xlabel('')
ax[1].set_xlabel('')
ax[2].set_xlabel('')
ax[1].set_ylabel('irregular [s]')
ax[2].set_ylabel('normal [s]')
plt.tight_layout()
plt.show()

