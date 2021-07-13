import pandas as pd 
import statistics
import csv

df = pd.read_csv('StudentsPerformance.csv')
ml = df['math score'].to_list()
rl = df['reading score'].to_list() 
wl = df['writing score'].to_list() 

mm = statistics.mean(ml)
rm = statistics.mean(rl)
wm = statistics.mean(wl)

mmed = statistics.median(ml)
rmed = statistics.median(rl)
wmed = statistics.median(wl)

mmode = statistics.mode(ml)
rmode = statistics.mode(rl)
wmode = statistics.mode(wl)

ms = statistics.stdev(ml)
rs = statistics.stdev(rl)
ws = statistics.stdev(wl)

print('mean, median and mode of math score is {}, {} and {}'.format(mm, mmed, mmode))
print('mean, median and mode of reading score is {}, {} and {}'.format(rm, rmed, rmode))
print('mean, median and mode of writing score is {}, {} and {}'.format(wm, wmed, wmode))

m1sds, m1sde = mm - ms, mm + ms
m2sds, m2sde = mm - (2*ms), mm + (2*ms)
m3sds, m3sde = mm - (3*ms), mm + (3*ms) 

r1sds, r1sde = rm - rs, rm + rs
r2sds, r2sde = rm - (2*rs), rm + (2*rs)
r3sds, r3sde = rm - (3*rs), rm + (3*rs) 

w1sds, w1sde = wm - ws, wm + ws
w2sds, w2sde = wm - (2*ws), wm + (2*ws)
w3sds, w3sde = wm - (3*ws), wm + (3*ws) 

mlist1std = [result for result in ml if result > m1sds and result < m1sde]
mlist2std = [result for result in ml if result > m2sds and result < m2sde]
mlist3std = [result for result in ml if result > m3sds and result < m3sde]

rlist1std = [result for result in rl if result > r1sds and result < r1sde]
rlist2std = [result for result in rl if result > r2sds and result < r2sde]
rlist3std = [result for result in rl if result > r3sds and result < r3sde]

wlist1std = [result for result in wl if result > w1sds and result < w1sde]
wlist2std = [result for result in wl if result > w2sds and result < w2sde]
wlist3std = [result for result in wl if result > w3sds and result < w3sde]

print('{}% of data for math score lies within one standard deviation'.format(len(mlist1std)*100.0/len(ml)))
print('{}% of data for math score lies within two standard deviation'.format(len(mlist2std)*100.0/len(ml)))
print('{}% of data for math score lies within three standard deviation'.format(len(mlist3std)*100.0/len(ml)))

print('{}% of data for reading score lies within one standard deviation'.format(len(rlist1std)*100.0/len(rl)))
print('{}% of data for reading score lies within two standard deviation'.format(len(rlist2std)*100.0/len(rl)))
print('{}% of data for reading score lies within three standard deviation'.format(len(rlist3std)*100.0/len(rl)))

print('{}% of data for writing score lies within one standard deviation'.format(len(wlist1std)*100.0/len(wl)))
print('{}% of data for writing score lies within two standard deviation'.format(len(wlist2std)*100.0/len(wl)))
print('{}% of data for writing score lies within three standard deviation'.format(len(wlist3std)*100.0/len(wl)))