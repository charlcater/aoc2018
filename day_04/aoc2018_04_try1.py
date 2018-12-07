# Advent of Code 2018
# Day 04: Repose Record -- Part 1

import numpy as np
import pandas as pd
import parse

# dataframes go as dataframe.iloc = [row, column]
# [1518-11-01 00:00] Guard #10 begins shift  --  entry format

snooze_matcher = '[{datetime:ti}] {act}'
time_matcher = '[{y:d}-{m:d}-{d:d} {hour:d}:{min:d}] {act}'
guard_matcher = 'Guard #{id:d} begins shift'

shiftlist = pd.DataFrame(columns=['datetime', 'ts', 'hour', 'min', 'action'])
minutelist = pd.DataFrame(columns=['hour', 'min'])


with open('input.txt', 'r') as f:

    for i, line in enumerate(f):
        line = line.replace('15', '17')  # move to pandas' date range :/

        p = parse.parse(snooze_matcher, line)
        pt = parse.parse(time_matcher, line)
        shift = np.array([p['datetime'], 0, pt['hour'], pt['min'], p['act']])
        shiftlist.loc[i] = shift

    shiftlist['ts'] = shiftlist[['datetime']].apply(lambda x: x[0].timestamp(), axis=1).astype(int)
    shiftlist.sort_values(['ts'], ascending=True, inplace=True)
    shiftlist.reset_index(inplace=True)

# print((shiftlist['ts']+7926076800)/60)
# print(shiftlist)

sleepytime = pd.DataFrame(1, index=np.arange(0), columns=['id', 'numshifts', 'time awake', 'time asleep'])
sleepytime.id = sleepytime.id.astype(str)

j = 0  # rowcount
s = 0

for i, row in shiftlist.iterrows():
    # print('i = {}'.format(i))
    if 'Guard' in row['action']:
        g = parse.parse(guard_matcher, row['action'])
        guardid = g['id']
        guardlist = [guardid]
        # print(guardid)
        awake = 0
        asleep = 0

        if sleepytime.iloc[:, 0].isin(guardlist).any():
            # print('{} again'.format(guardid))

            for srow in range(sleepytime.shape[0]):
                if sleepytime.iloc[srow][0] == guardid:
                    sleepytime.iloc[srow, 1] += 1
                    onguard = True

                    s = 0
                    while onguard is True:

                        try:
                            if shiftlist.iloc[i+s+1][5] == 'falls asleep':
                                # print('falls asleep')
                                # print('Guard #{} falls asleep'.format(guardid))
                                awake = int((shiftlist.iloc[i+s+1][2] - shiftlist.iloc[i+s][2])/60)
                                sleepytime.iloc[srow, 2] += awake
                                # print('awake = {} minutes'.format(awake))
                                s+=1

                            elif shiftlist.iloc[i+s+1][5] == 'wakes up':
                                # print('wakes up')
                                # print('Guard #{} wakes up'.format(guardid))
                                asleep = int((shiftlist.iloc[i+s+1][2] - shiftlist.iloc[i+s][2])/60)
                                sleepytime.iloc[srow, 3] += asleep
                                # print('asleep = {} minutes'.format(asleep))
                                s+=1
                            else:
                                # print('end shift')
                                # print('Guard #{} end shift'.format(guardid))
                                # awake += int((shiftlist.iloc[i+s+1][2] - shiftlist.iloc[i+s][2])/60)
                                awake = 60 - shiftlist.iloc[i+s][4]
                                # print('final minutes {}'.format(awake))
                                # print('awake = {} minutes'.format(awake))
                                sleepytime.iloc[srow, 2] += awake
                                onguard = False

                        except Exception as ex:
                            awake = 60 - shiftlist.iloc[i+s][4]
                            # print('final minutes {}'.format(awake))
                            sleepytime.iloc[srow, 2] += awake
                            print('EOF')
                            break
            else:
                pass

        else:  # add row to sleepytime
            # print('adding {}'.format(guardid))
            sleepytime = sleepytime.append({'id': guardid}, ignore_index=True)
            sleepytime.iloc[j, 1] = 1
            sleepytime.iloc[j, 2] = 0
            sleepytime.iloc[j, 3] = 0
            firstshift = True

            s = 0
            while firstshift is True:

                if shiftlist.iloc[i+s+1][5] == 'falls asleep':
                    # print('falls asleep')
                    # print('{} Guard #{} falls asleep 1'.format(s, guardid))
                    awake = int((shiftlist.iloc[i+s+1][2] - shiftlist.iloc[i+s][2])/60)
                    sleepytime.iloc[j, 2] += awake
                    # # print('awake = {} minutes'.format(awake))
                elif shiftlist.iloc[i+s+1][5] == 'wakes up':
                    # print('wakes up')
                    # print('{} Guard #{} wakes up 1'.format(s, guardid))
                    asleep = int((shiftlist.iloc[i+s+1][2] - shiftlist.iloc[i+s][2])/60)
                    sleepytime.iloc[j, 3] += asleep
                    # # print('asleep = {} minutes'.format(asleep))
                else:
                    # print('end shift')
                    # print('{} Guard #{} end shift 1'.format(s, guardid))
                    # awake += int((shiftlist.iloc[i+s+1][2] - shiftlist.iloc[i+s][2])/60)
                    awake = 60 - shiftlist.iloc[i + s][4]
                    # print('final minutes {}'.format(awake))
                    # # print('awake = {} minutes'.format(awake))
                    sleepytime.iloc[j, 2] += awake
                    firstshift = False

                s += 1
            j += 1
            # print(sleepytime)
            # print('')
    else:
        pass

sleepytime['id'] = sleepytime['id'].apply(np.int64)
sleepytime['numshifts'] = sleepytime['numshifts'].apply(np.int64)
sleepytime['time awake'] = sleepytime['time awake'].apply(np.int64)
sleepytime['time asleep'] = sleepytime['time asleep'].apply(np.int64)
sleepytime.sort_values(['time asleep'], ascending=False, inplace=True)
print(sleepytime)
