#!/usr/bin/env python3
#
# Times logged as 1 or "on" characterized by loud snoring, irregular/labored breathing, and gasping
# Times logged as 0 or "off" indicate regular breathing or an absence of snoring
#
# Written by Eliot Quon (11/28/17)
#
import datetime

curtime = datetime.datetime.now()
dtstr = curtime.strftime('%Y%m%d_%H%M%S')

with open('log.sleep.'+dtstr,'a') as f:
    while True:
        state = input('state (o/x)? ')
        tstr = str(datetime.datetime.now())
        if state.strip().startswith('o'):
            print(f'STARTED at {tstr}')
            f.write(f'"{tstr}" 0\n')
            f.write(f'"{tstr}" 1\n')
        elif state.strip().startswith('x'):
            print(f'...STOPPED at {tstr}')
            f.write(f'"{tstr}" 1\n')
            f.write(f'"{tstr}" 0\n')

