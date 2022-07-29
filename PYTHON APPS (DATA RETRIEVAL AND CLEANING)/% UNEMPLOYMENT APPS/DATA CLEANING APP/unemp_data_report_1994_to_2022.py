import json
import csv
import pandas as pd

table1 = pd.read_csv (r'./CLEAN DATA/% Unemployment/Data File/clean_unemp_data_report_1994_to_2000.csv')
table2 = pd.read_csv (r'./CLEAN DATA/% Unemployment/Data File/clean_unemp_data_report_2001_to_2010.csv')
table3 = pd.read_csv (r'./CLEAN DATA/% Unemployment/Data File/clean_unemp_data_report_2011_to_2022.csv')

#Concat to data frames that share common columns
# load in the various tables from an excel document

joint_table = pd.concat([table3,table2,table1])


joint_table.to_csv('./CLEAN DATA/% Unemployment/Data File/clean_unemp_data_report_1994_to_2022.csv')