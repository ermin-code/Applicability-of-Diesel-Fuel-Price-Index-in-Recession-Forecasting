import json
from c_bls_data_api import c_bls_data_api

# Call c_bls_data_api.py with a request for CPI data from 2002 through 2021
# and the name of the file to store the returned JSON data structure in.

print("Program started...")

# Set the register, series ID for CPI, start year, end year, and calculations. Note that setting calculations to true
# returns CPI percentages as well as the raw CPI.

parameters1 = json.dumps({"registrationkey":"64ea89c953c14b98a90b9beca800748a", "seriesid":['CUUR0000SA0'], "startyear":"1994", "endyear":"2000", "calculations":"true"})
parameters2 = json.dumps({"registrationkey":"64ea89c953c14b98a90b9beca800748a", "seriesid":['CUUR0000SA0'], "startyear":"2001", "endyear":"2010", "calculations":"true"})
parameters3 = json.dumps({"registrationkey":"64ea89c953c14b98a90b9beca800748a", "seriesid":['CUUR0000SA0'], "startyear":"2011", "endyear":"2022", "calculations":"true"})

# Call the bls data api class with the parameters and the name of the data output file.
c_bls_data_api(parameters1, './RAW DATA/Consumer Price Index (CPI)/Data File/cpi_data_report_1994_to_2000.json')
c_bls_data_api(parameters2, './RAW DATA/Consumer Price Index (CPI)/Data File/cpi_data_report_2001_to_2010.json')
c_bls_data_api(parameters2, './RAW DATA/Consumer Price Index (CPI)/Data File/cpi_data_report_2011_to_2022.json')

print("Program completed...")