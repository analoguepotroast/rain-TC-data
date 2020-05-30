import pandas as pd
import numpy as np
import time
start =time.clock()

#this is a time-consuming process such that the whole flood event file was divided into four parts (1,2,3,4).
#for every flood event excelsheet (4 in total), the flood event counts are 20,000.
#define timeline
def parse(x):
    try:
        return pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    except:
        return pd.datetime.strptime(x, '%m/%d/%Y %H:%M')

#import data
df1 = pd.read_excel(r'C:\Users\lxiao\Desktop\A.xlsx', header=0, parse_dates=['BEGIN_DATE_TIME(UTC)'], sheet_name='4', date_parser=parse)
df2 = pd.read_excel(r'C:\Users\lxiao\Desktop\B.xlsx', header=0, parse_dates=['ISO_time'], date_parser=parse)
matrix = np.zeros((df1.shape[0], 3))
df3 = pd.DataFrame(matrix)
df3.columns = ['EVENT_ID', 'TRACK_ID', 'Diff']
file = r'C:\Users\lxiao\Desktop\4.csv'

#loop all flood events associated to each hurricane track point.
# flood events will be selected if if they occured within 7 days after a hurricane stroke.
for i in range(df1.shape[0]):
    a = 1000000000
    for j in range(df2.shape[0]):
        t = df1.iloc[i]['BEGIN_DATE_TIME(UTC)'] - df2.iloc[j]['ISO_time']
        diff = abs(t.seconds) + abs(t.days * 86400)
        if int(abs(t.days)) <= 7 and a > diff:
            a = diff
            df3.iloc[i]['Diff'] = a
            df3.iloc[i]['EVENT_ID'] = df1.iloc[i]['EVENT_ID']
            df3.iloc[i]['TRACK_ID'] = df2.iloc[j]['TRACK_ID']
    print(i)

#export data
df3.to_csv(file, header=True, index=None, sep=' ')
end = time.clock()
print('Running time: %s Seconds'%(end-start))




