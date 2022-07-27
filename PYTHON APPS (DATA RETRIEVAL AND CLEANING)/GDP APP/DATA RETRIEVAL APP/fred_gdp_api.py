import fredapi as fa

fred = fa.Fred(api_key='a2bd6683c9adb16b19eace52772289a5')

df = fred.get_series('GDP')

df.tail()

df.to_csv('./RAW DATA/Gross Domestic Product (GDP)/Data File/gdp_data.csv')
