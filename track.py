import pandas as pd

#Define a function to convert date information to python timestamp
def parse(x):
    try:
        return pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    except:
        return pd.datetime.strptime(x, '%m/%d/%Y %H:%M')

#Before run the following lines, 1995-2014_Track_Index file should be generated first
#1995-2014_Track_Index was created by removing dupilicates from original file: 1995-2014_Track
#Read excelsheets one by one and create dataframes for each excelsheet
data = pd.read_csv(r'E:\temp\NewIdea\PhD\New\1995-2014_Track_Index.csv', header=0)
area_list=list(set(data[u'Serial_Num']))
c = []
df3 = pd.DataFrame(c).astype(float)
for i in sorted(area_list):
    print(i)
    #Create dataframes based on different excelsheets
    series = pd.read_excel(r'E:\temp\NewIdea\PhD\New\1995-2014_Track_Split.xlsx',
                          sheet_name=i, header=0, parse_dates=[1], date_parser=parse)
    #Set series index before interpolation
    df1 = series.set_index(pd.DatetimeIndex(pd.to_datetime(series.ISO_time)))
    #Unsample time series data by 1 hour
    upsampled = df1.resample('H')
    rowscount = len(df1.index)
    #Use different interpolate method according to different hurricane records
    if rowscount <= 4:
        interpolated = upsampled.interpolate(method='linear')
    else:
        interpolated = upsampled.interpolate(method='cubic', order=2)
    #Round digit number and fill null values in dataframes
    Digit = round(interpolated,2)
    fill = Digit.fillna(method='ffill')
    df2 = pd.DataFrame(fill)
    del df2['ISO_time']
    #Merge dataframes
    df3 = pd.concat([df3, df2], axis=0)
    print(df3)
#Export dataframe to csv file
df3.to_csv(r'C:\Users\lxiao\Desktop\Result.csv', header=True, index=True, sep=' ')

