import json
import csv
import pandas as pd


import numpy as np

with open('./RAW DATA/% Unemployment/Data File/unemp_data_report_1994_to_2000.json') as json_file:
    data = json.load(json_file)
 
    df = data['Results']['series']


    df_deep = pd.DataFrame(df)

df_deep = df_deep.drop('seriesID', axis=1)

df_dict = dict(df_deep)

dataframe = df_dict['data']

dataframe_dict = dict(dataframe)

dataframe_final = pd.DataFrame(dataframe_dict)

dataframe_final = dataframe_final.rename(columns={0: "Data"})

dataframe_final = dataframe_final.astype(str)

dataframe_final_split1 = dataframe_final['Data'].str.split(',', expand=True)

dataframe_final_split1 = dataframe_final_split1.rename(columns={0: "Year",1: "Period",2: "Period Name",3: "Value",4: "Footnotes"})

dataframe_final_Year = dataframe_final_split1['Year'].str.split(':', expand=True)

dataframe_final_Year = dataframe_final_Year.rename(columns={1: "Year"})

dataframe_final_Year = pd.DataFrame(dataframe_final_Year)

dataframe_final_Year = dataframe_final_Year.rename(columns={0: "ID", 1: "Year"})

dataframe_final_Year.drop('ID', inplace=True, axis=1)



dataframe_final_Year = dataframe_final_Year.reset_index()
dataframe_final_Year = dataframe_final_Year.rename(columns={"index":"New_ID"})
dataframe_final_Year['New_ID'] = dataframe_final_Year.index + 1





dataframe_final_Period = dataframe_final_split1['Period'].str.split(':', expand=True)

dataframe_final_Period = dataframe_final_Period.rename(columns={1: "Period"})

dataframe_final_Period = pd.DataFrame(dataframe_final_Period)

dataframe_final_Period = dataframe_final_Period.rename(columns={0: "ID", 1: "Period"})


dataframe_final_Period.drop('ID', inplace=True, axis=1)


dataframe_final_Period = dataframe_final_Period.reset_index()
dataframe_final_Period = dataframe_final_Period.rename(columns={"index":"New_ID"})
dataframe_final_Period['New_ID'] = dataframe_final_Period.index + 1



dataframe_final_Value = dataframe_final_split1['Value'].str.split(':', expand=True)

dataframe_final_Value = dataframe_final_Value.rename(columns={1: "Value"})

dataframe_final_Value = pd.DataFrame(dataframe_final_Value)

dataframe_final_Value = dataframe_final_Value.rename(columns={0: "ID", 1: "Value"})


dataframe_final_Value.drop('ID', inplace=True, axis=1)

dataframe_final_Value = dataframe_final_Value.reset_index()
dataframe_final_Value = dataframe_final_Value.rename(columns={"index":"New_ID"})
dataframe_final_Value['New_ID'] = dataframe_final_Value.index + 1

dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M01', '01/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M02', '02/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M03', '03/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M04', '04/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M05', '05/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M06', '06/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M07', '07/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M08', '08/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M09', '09/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M10', '10/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M11', '11/01')
dataframe_final_Period["Period"] = dataframe_final_Period["Period"].str.replace('M12', '12/01')

dataframe_final_Value['Value'] = [i.replace("'","") for i in dataframe_final_Value['Value']]

dataframe_final_Period['Period'] = [i.replace("'","") for i in dataframe_final_Period['Period']]

dataframe_final_Year['Year'] = [i.replace("'","") for i in dataframe_final_Year['Year']]

df_merge = dataframe_final_Year.merge(dataframe_final_Period, on='New_ID')

df_merge1 = df_merge.merge(dataframe_final_Value, on='New_ID', how='right')







df_merge1["Date"] = dataframe_final_Period['Period'].astype(str) +'/'+ dataframe_final_Year['Year'].astype(str)






#df_merge1["Date"] = pd.to_datetime(df_merge1["Date"], format='%m%d%y')

df_merge1.to_csv('./CLEAN DATA/% Unemployment/Data File/clean_unemp_data_report_1994_to_2000.csv')


