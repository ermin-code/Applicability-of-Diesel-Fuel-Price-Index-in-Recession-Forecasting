import fredapi as fa

fred = fa.Fred(api_key='Ask Me')

df = fred.get_series('GDP')

df.tail()

df.to_csv('./RAW DATA/Gross Domestic Product (GDP)/Data File/gdp_data.csv')
