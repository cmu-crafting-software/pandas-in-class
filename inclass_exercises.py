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