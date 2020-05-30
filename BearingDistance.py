import math
import pandas as pd
from haversine import haversine

x1 = 0
y1 = 0
x2 = 1
y2 = -2

#bearing distance function
def Bearing(x1, y1, x2, y2):
    angle = 0
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
        if y2 == y1:
            angle = 0.0
        elif y2 < y1:
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif x2 < x1 and y2 > y1:
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1:
        angle = math.pi + math.atan(dx / dy)
    elif x2 > x1 and y2 < y1:
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return (angle * 180 / math.pi)


#Data input
df = pd.read_csv(r'C:\Users\lxiao\Desktop\Matyas\Event_Selected_Joined.csv', header=0)
df = pd.concat([df, pd.DataFrame(columns=list('DB'))])
out = r'C:\Users\lxiao\Desktop\Matyas\BearingDistance.csv'
for i in range(df.shape[0]):
    x1 = float(df.iloc[i]['Hurricane_Long'])
    y1 = float(df.iloc[i]['Hurricane_Lat'])
    x2 = float(df.iloc[i]['Event_Long'])
    y2 = float(df.iloc[i]['Event_Lat'])
    # Distance
    df['D'].iloc[i] = haversine((x1, y1), (x2, y2))
    #Bearing
    df['B'].iloc[i] = Bearing(x1, y1, x2, y2)
    print(i)
df.to_csv(out, header=True, index=None, sep=' ')