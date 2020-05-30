import pandas as pd
#Data configs
#Original track file is 1995-2014_Track.csv (ibtracs_na_1995.csv)
data=pd.read_csv(r'E:\temp\NewIdea\PhD\New\1995-2014_Track.csv', header=0)
area_list=list(set(data[u'Serial_Num']))
#Generate a new excel file containing multiple excelsheets based on 'Serial_Num' field
with pd.ExcelWriter(r'E:\temp\NewIdea\PhD\New\1995-2014_Track_Split.xlsx') as writer:
    for j in area_list:
        print(j)
        df=data[data[u'Serial_Num']==j]
        df.to_excel(writer,sheet_name=j,index=False)
