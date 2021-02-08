import pandas as pd 

# data = {'Month': pd.Series(['January','February','March','April','May','June','July','August','September',
# 'October','November','December']),
# 'Rainfall':pd.Series([1.65,1.25,1.94,2.75,2.75,3.65,5.05,1.50,1.33,0.07,0.50,2.30]),
# }

# create dataframe
#df = pd.DataFrame(data)
df = pd.read_csv('coursera_classes/processing data with python/rain.csv')

print(df,'\n')

# fill in the missing values with zeros
#dfzeros = df.fillna(0)
#print(dfzeros)

# remove the rows with missing values
dfclean = df.dropna()
print(dfclean)

# count all rows containing Nans
count = 0
for index, row in df.iterrows():
    if any(row.isnull()):
        count += 1
# print('\nNumber of rows with NaNs: ' + str(count))

# print('Mean data: ')
# print(dfclean.mean())
# print('\nmedian')
# print(dfclean.median())
# print('\nstandard deviation')
# print(dfclean.std())

# print the rainfall and mean for tirst few months
rainfall = dfclean['Rainfall'][0:3]
print(rainfall)
print('mean rainfall: ',rainfall.mean(),'\n')

print('\n Just temp and rainfall data')

dfTempRain = (dfclean[['Tempurature','Rainfall']])
print(dfTempRain)
print('mean:\n', dfTempRain.mean())

index = dfclean['Month']
dfIndexed = dfclean.set_index(index)
#requires a properly indexed dataframe
print('Finds a row by value \n', dfIndexed.loc['March'])
