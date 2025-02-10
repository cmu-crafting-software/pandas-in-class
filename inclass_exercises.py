import pandas as pd

## 1. Write an expression to find the Per Capita GDP of Serbia in 2007.
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(f'GPD of Serbia in 2007: {europe_gdp_data.loc['Serbia', 'gdpPercap_2007']}')


# 2. Explain what each line in the following short program does: 
# first = pd.read_csv('data/gapminder_all.csv', index_col='country')
# second = first[first['continent'] == 'Americas']
# third = second.drop('Puerto Rico')
# fourth = third.drop('continent', axis = 1)
# fourth.to_csv('result.csv')

'''
first --> reads in gdp data over time, and indexes (sorts) the data based on country
second --> isolates the dataframe to only countries that have index 'americas' in the continent column, stores in new object
third --> Remotes the column for Puerto Rico from the dataframe, stores it in new object
fourth --> removes the column for continent, and saves it into a new object
fourth.to_csv() --> saves new, filtered dataframe into results.csv file
'''


# 3. a) Do the second and third lines below produce the same output? 
'''
No, they produce different outputs.
first print command
         gdpPercap_1952  gdpPercap_1957
country                                
Albania     1601.056136     1942.284244
Austria     6137.076492     8842.598030

second print command
         gdpPercap_1952  gdpPercap_1957  gdpPercap_1962
country                                                
Albania     1601.056136     1942.284244     2312.888958
Austria     6137.076492     8842.598030    10750.721110
Belgium     8343.105127     9714.960623    10991.206760

'''
# 3. b) Based on this, what rule governs what is included (or not) in numerical slices and named slices in Pandas?
'''
Numerical slices include the starting index, and end up to the final index -1. So indexing between 0:2 retrieves indices
0 and 1, but not 2.

Conversely, using named slices includes the starting and the ending indices, unlike the nmerical slicing method.
'''


print(europe_gdp_data.iloc[0:2, 0:2])
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

# 4. Stretch Goal: 
# Write an expression to select each of the following:
#     * GDP per capita for all countries in 1982.
#     * GDP per capita for Denmark for all years.
#     * GDP per capita for all countries for years after 1985.
#     * GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.

all_gdp_data = pd.read_csv('data/gapminder_all.csv', index_col='country')
print('GDP FOR ALL COUNTRIES IN 1982')
print(all_gdp_data.loc[:,'gdpPercap_1982'])


denmark_gdp = europe_gdp_data.loc['Denmark']
print('DENMARK GDP OVER TIME')
print(denmark_gdp)

print('GDP FOR ALL COUNTRIES AFTER 1985')
gdp_after_1985 = all_gdp_data.filter(regex='gdpPercap_(198[6-9]|199.|200.)')
print(gdp_after_1985)

print('GDP IN 2007 AS A MULTIPLE OF 1952')
print(all_gdp_data.loc[:,'gdpPercap_2007'] / all_gdp_data.loc[:,'gdpPercap_1952'])
