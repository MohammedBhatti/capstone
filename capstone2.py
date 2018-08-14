import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
plt.style.use('fivethirtyeight')
#%matplotlib inline

df = pd.read_csv('c:/code/data/mbb_teams_games_sr.csv')

# drop columns we don't need
df.drop(['game_id', 'status', 'coverage', 'logo_large', 'logo_medium', 'logo_small', 'possession_arrow', 'venue_id', 'team_id', 'league_id', 'conf_id', 'conf_name', 'division_name', 'opp_id', 'opp_league_id', 'opp_league_name', 'opp_conf_id', 'opp_conf_name', 'opp_division_id', 'opp_division_name', 'opp_logo_large', 'opp_logo_medium', 'opp_logo_small',], axis=1, inplace=True)

# do some analysis
print(df.head())
print(df.dtypes)
print(df.describe())
print(df.shape)
print(df.describe(include='all'))
print(df.columns)
#columns with nan values
df.loc[:, df.isna().any()]
count_nan = len(df) - df.count()
print('COUNT_NAN')
print(count_nan)

# lets plot wins/losses home vs away
df[['win','season']]
# groupby league_alias
#print(df[['league_alias']].groupby(['league_alias']).head())
#print(df[['league_alias']].groupby(['league_alias']).league_alias.value_counts())
print(df.groupby(['league_alias']).league_alias.value_counts())
print(df.groupby(['conf_alias']).conf_alias.value_counts())
#print(df.groupby(['status']).head())
#print(df.groupby(['season']).head())

# do we have anything other than 'closed' in the 'status' column?
# print(df[df[['status']]['status'] != 'closed'].head())

# covariance
print(df.cov())

# Calculate the correlation matrix using the default method.
print(df.corr())

sns.set_palette("coolwarm", 7)
sns_heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1)
fig = sns_heatmap.get_figure()
fig.savefig("output.png") 

# lets gather the features that we are interested in

# rename population columns
#pop_df.rename(columns={"2010 Census Population": "pop_2010", "Population Estimate, 2011": "pop_2011", "Population Estimate, 2012": "pop_2012", "Population Estimate, 2013": "pop_2013", "Population Estimate, 2014": "pop_2014", "Population Estimate, 2015": "pop_2015", "Population Estimate, 2016": "pop_2016"}, inplace = True)

# for population data, remove commas and convert to int
#for col in pop_df.columns[3:]:
#   pop_df[col] = pop_df[col].str.replace(',', '')
#   pop_df[col] = pop_df[col].astype(str).astype(int)

# get our shape
#pop_df.shape
#pop_df.describe(include='all')

# columns with nan values
#pop_df.loc[:, pop_df.isna().any()]
#count_nan = len(pop_df) - pop_df.count()

# popultaion >= 500000
#pop_df[pop_df.pop_2010 >= 500000]

# open health data
#health_df = pd.read_csv('c:/code/data/health_data.csv')
#health_df.columns

# join health_df to pop_df
#result = pd.concat([pop_df, health_df], axis=1, join='inner')

# keep only the columns we want
#result = result.loc[:,~result.columns.duplicated()]

#result.describe(include='all')

# columns with nan values
#result.loc[:, result.isna().any()]
#count_nan = len(result) - result.count()

# examine column counts
#result[['pop_2010', 'pop_2011', 'pop_2012']].head()

# create a dataframe for analysis
# df = result[['FIPS', 'State', 'County', ]]

# open our data that include population estimates for 2008 and 2009
#pop_df2 = pd.read_csv('c:/code/data/co-est2009-alldata.csv')

# drop columns we don't need
#pop_df2.drop(['SUMLEV', 'REGION', 'DIVISION', 'STATE'], axis=1, inplace=True)

# Only interested in counties, so filter where COUNTY > 0
#pop_df2 = pop_df2[pop_df2.COUNTY > 0]

# now, replace 'County' and 'Parish' in CTYNAME column with blank so we only have county/parish name
#pop_df2['CTYNAME'] = pop_df2['CTYNAME'].str.replace('County', '')
#pop_df2['CTYNAME'] = pop_df2['CTYNAME'].str.replace('Parish', '')

#pop_df2 = pop_df2.CTYNAME.str.replace('County', '')
#pop_df2 = pop_df2.CTYNAME.str.replace('Parish', '')

# check our data
#pop_df2[pop_df2.STNAME == 'Louisiana'].CTYNAME.head(10)

# https://www.census.gov/topics/education.html
# https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml#acsST
# https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_16_1YR_S1501&prodType=table
# HC02_EST_VC18	Percent; Estimate; Percent bachelor's degree or higher
# HC02_EST_VC17	Percent; Estimate; Percent high school graduate or higher
