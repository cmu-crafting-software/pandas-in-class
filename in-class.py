import pandas as pd

first = pd.read_csv('data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')

europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
# print(europe_gdp_data.iloc[0:2, 0:2])
# print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

data = pd.read_csv('data/gapminder_all.csv') # read the csv file as data
# 4a GDP per capita for all countries in 1982.
gdp_1982 = data[['country', 'gdpPercap_1982']]
print(gdp_1982)

# 4b GDP per capita for Denmark for all years.
denmark_data = data[data['country'] == 'Denmark']
denmark_gdp = denmark_data.filter(regex='gdpPercap_.*').transpose() # transpose for easier reading
denmark_gdp.index = denmark_gdp.index.str.replace('gdpPercap_', '') # remove the gdpPercap for easier reading
denmark_gdp.columns = ['GDP per Capita']
print(denmark_gdp)

# 4c GDP per capita for all countries for years after 1985.
gdp_after_1985 = data.filter(regex='gdpPercap_(198[7-9]|199.|200.)')
gdp_after_1985.insert(0, 'Country', data['country'])  # adding country column for reference
print(gdp_after_1985)

# 4d GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.
gdp_multiple = data['gdpPercap_2007'] / data['gdpPercap_1952']
gdp_multiple_df = pd.DataFrame({'Country': data['country'], 'Multiple': gdp_multiple})
print(gdp_multiple_df)

