import json
import csv
import pandas as pd

# Loading JSON file from RAW DATA/Consumer Price Index (CPI)/Data File folder into Pandas dataframe

with open('./RAW DATA/Consumer Price Index (CPI)/Data File/cpi_data_report_1994_to_2000.json') as json_file:
    data = json.load(json_file)
 

 # Removes 'Results' and 'series' series from 'data' dataframe
    
    df = data['Results']['series']


# Converts 'df' dataframe into Pandas 'df_deep' dataframe

    df_deep = pd.DataFrame(df)

# Removes 'seriesID' column from Pandas 'df_deep' dataframe

df_deep = df_deep.drop('seriesID', axis=1)

# Converts 'df_deep' into 'df_dict' dictionary

df_dict = dict(df_deep)

# Converts 'df_dict' dictionary into 'dataframe' Pandas dataframe
dataframe = df_dict['data']

# Converts 'dataframe' dataframe into 'dataframe' dictionary
dataframe_dict = dict(dataframe)

# Converts 'dataframe' dictionary into 'dataframe_dict' Pandas dataframe
dataframe_final = pd.DataFrame(dataframe_dict)

# Renames column '0' in dataframe_final Pandas dataframe to 'Data'
dataframe_final = dataframe_final.rename(columns={0: "Data"})

# Converts 'dataframe_final' values to strings
dataframe_final = dataframe_final.astype(str)

# Splits 'Data' column in 'dataframe_final' to two columns 
dataframe_final_split1 = dataframe_final['Data'].str.split(',', expand=True)

# Renames four columns in dataframe_final_split1 Pandas dataframe to 'Year', 'Period', 'Period Name', 'Value' and 'Footnotes'
dataframe_final_split1 = dataframe_final_split1.rename(columns={0: "Year",1: "Period",2: "Period Name",3: "Value",4: "Footnotes"})

# Splits 'Year' column
dataframe_final_Year = dataframe_final_split1['Year'].str.split(':', expand=True)

# Renames column 1 to Year
dataframe_final_Year = dataframe_final_Year.rename(columns={1: "Year"})

# Converts dataframe_final_Year
dataframe_final_Year = pd.DataFrame(dataframe_final_Year)

# Renames columns in dataframe_final_Year Pandas dataframe to 'ID' and 'Year'
dataframe_final_Year = dataframe_final_Year.rename(columns={0: "ID", 1: "Year"})

# Removes 'ID' column from dataframe_final_Year dateframe
dataframe_final_Year.drop('ID', inplace=True, axis=1)


# Creates New_ID index column as a reference when merging other columns
dataframe_final_Year = dataframe_final_Year.reset_index()
dataframe_final_Year = dataframe_final_Year.rename(columns={"index":"New_ID"})
dataframe_final_Year['New_ID'] = dataframe_final_Year.index + 1

# Splits 'Period' column in dataframe_final_Period
dataframe_final_Period = dataframe_final_split1['Period'].str.split(':', expand=True)

# Renames column '1' to 'Period' in dataframe_final_Period
dataframe_final_Period = dataframe_final_Period.rename(columns={1: "Period"})

# Sets dataframe_final_Period as a Pandas dataframe
dataframe_final_Period = pd.DataFrame(dataframe_final_Period)

# Renames columns '0' and '1' in dataframe_final_Period to 'ID' and 'Period'
dataframe_final_Period = dataframe_final_Period.rename(columns={0: "ID", 1: "Period"})

# Removes 'ID' column form dataframe_final_Period dataframe
dataframe_final_Period.drop('ID', inplace=True, axis=1)

# Creates a 'New_ID' column as a reference when merging columns
dataframe_final_Period = dataframe_final_Period.reset_index()
dataframe_final_Period = dataframe_final_Period.rename(columns={"index":"New_ID"})
dataframe_final_Period['New_ID'] = dataframe_final_Period.index + 1

# Splits 'Value' column
dataframe_final_Value = dataframe_final_split1['Value'].str.split(':', expand=True)

# Renames column "1" to 'Value' column in dataframe_final_Value
dataframe_final_Value = dataframe_final_Value.rename(columns={1: "Value"})

# Sets dataframe_final_Value as a Pandas dataframe
dataframe_final_Value = pd.DataFrame(dataframe_final_Value)

# Renames '0' and '1' columns in dataframe_final_Value to 'ID' and 'Value'
dataframe_final_Value = dataframe_final_Value.rename(columns={0: "ID", 1: "Value"})

# Removes 'ID' column from dataframe_final_Value dataframe
dataframe_final_Value.drop('ID', inplace=True, axis=1)

# Sets New_ID column as an index reference column when merging columns
dataframe_final_Value = dataframe_final_Value.reset_index()
dataframe_final_Value = dataframe_final_Value.rename(columns={"index":"New_ID"})
dataframe_final_Value['New_ID'] = dataframe_final_Value.index + 1

# Converts M01 through M12 in 'Period' column of dataframe_final_Period dataframe to month/date values
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

# Removes '' quotes from string values in columns
dataframe_final_Value['Value'] = [i.replace("'","") for i in dataframe_final_Value['Value']]

dataframe_final_Period['Period'] = [i.replace("'","") for i in dataframe_final_Period['Period']]

dataframe_final_Year['Year'] = [i.replace("'","") for i in dataframe_final_Year['Year']]


# Merges dataframe_final_Value, dataframe_final_Period and dataframe_final_Year together into 
# df_merge1 dataframe
df_merge = dataframe_final_Year.merge(dataframe_final_Period, on='New_ID')

df_merge1 = df_merge.merge(dataframe_final_Value, on='New_ID', how='right')

# Adds 'Period' and 'Year' columns into one 'Date' column to form a date to be used in Tableau
df_merge1["Date"] = dataframe_final_Period['Period'].astype(str) +'/'+ dataframe_final_Year['Year'].astype(str)

# Exports df_merge1 final dataframe into csv file located in /CLEAN DATA/Consumer Price Index (CPI)/Data File folder
df_merge1.to_csv('./CLEAN DATA/Consumer Price Index (CPI)/Data File/clean_cpi_data_report_1994_to_2000.csv')


# PLEASE NOTE THAT Cleaning Apps for CPI and % Unemployment are nearly identical. Explanation written
# here applies to % Unemployment Cleaning Apps as well...