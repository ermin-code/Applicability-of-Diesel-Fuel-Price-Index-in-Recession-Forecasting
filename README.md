Applicability of Diesel Fuel-Price Index in Recession Forecasting (a Code Louisville Project)

This project was created to satisfy Code Louisville requirements for completing Python/Data Analytics track. Technologies that were used in this project are: 
Python, Pandas library for data cleaning and manipulation and Tableau for data visualization. The main goal of this project was to demonstrate that diesel fuel
prices have a major impact on our economy and can be considered as a viable economic indicator in recession forecasting models. Diesel engines in trucks, trains,
boats, and barges help transport nearly all products people consume. Diesel fuel is commonly used in public buses and school buses, and it powers most of the farm 
and construction equipment in the United States. As such, it has a significant effect on major sectors of the U.S economy. The dashboard that was constructed in this
project demonstrates the relationship between Diesel Fuel Price Index and Consumer Price Index (CPI) as well as 10-Year Yield Market Curve. Yield Curve has been one
of the best predictors of recession while CPI has been a reliable predictor of inflation. I also included a graph showing % unemployment over the years and it can
be compared to other data that is on the dashboard. 

How data is gathered: 
For CPI and % Unemployment, I used the API that was available on the U.S. Bureau of Labor Statistics(www.bls.gov), for GDP and Yield Curve I used FRED source. Data
that I used for Diesel Fuel Price Index was accessible through EIA Web Data Connector source at https://wdc.portals.interworks.com/eia_20/ .

Data Organization:
I tried to organize the data as neatly as possible. RAW DATA folders contain raw API pulls that are either in .csv or .json formats. CLEAN DATA contains .csv or .json
files that already have been processed by data cleaning Python scripts that I created. Python scripts are organized in PYTHON APPS folder. Once you select specific folder
inside of PYTHON APPS folder, you will see DATA GATHERING APPS and DATA CLEANING APPS folders. Python scripts that I made to retrieve raw API data are in DATA 
GATHERING APPS folder while scripts that I made for cleaning raw data are in DATA CLEANING APPS folders. To gather data, there are two main scripts, c_bls_data_api.py and
retireve_bls_unemp_data.py. These names are similar for to the scripts in CPI Data Cleaning folder. You first need to run c_bls_data_api.py script in order to set 
retrieval parameters for retrieve_bls_unemp_data.py to use in order to gather API raw data. After retrieve_bls_unemp_data.py runs, it will store raw data into RAW DATA
folder specific to the data type. Data cleaning Python scripts are pretty straight forward. They will pull in the raw data from RAW DATA folders automatically, clean & 
process and store them in CLEAN DATA folders to be uploaded into Tableau. Data cleaning python scripts that are dated 1994 to 2022 contain a data stitching script that
compiles all the data into one file labeled 1994_to_2022. That is the file that was uploaded into Tableau to create the dashboard. 

Methods that were used in creating this project should satisfy all the requirements needed to complete Code Louisville Analytics/Python Data 2 course. Those include, 
pull of data through an API source, cleaning & stitching of dataframes and exporting them in csv and json files as well as visualizing the processed data through a
Tableau dashboard. 

The Tableau workbook file consists of Diesel Fuel Index vs. Time, Consumer Price Index (CPI) vs Time, Market Yield Curve vs Time, Percent of Unemployment vs Time, Gross
Domestic Product vs Time, Diesel Fuel Price Index vs CPI as vs 10-Year Market Yield Curve in 2-dimensional graphs over time. It also includes a Tableau dashboard that consists
of % Unemployment vs Time, GDP vs Time as well as Diesel Fuel Price Index vs CPI and vs 10-Year Yield Market Curve.

Data Sources:

Percent Unemployment API Data:

https://api.bls.gov/publicAPI/v2/timeseries/data/

CPI (Consumer Price Index) API Data:

https://api.bls.gov/publicAPI/v2/timeseries/data/

GDP (Gross Domestic Product) Data:

https://fred.stlouisfed.org/

Diesel Fuel Price Index Data:

https://www.eia.gov/


Thank you for reviewing my project. If you have any specific questions about it, please do not hesitate to contact me on my email address at erminky@gmail.com


Ermin Vila - All Rights Reserved.
