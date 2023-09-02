import pandas as pd


# Load processed data
df = pd.read_csv('./data/hills_etl.csv')

# Calculate mountain types by country
df_simms_by_country = df.groupby('Country').sum()[['Ma', 'Hu', 'Sim', 'P600']]
df_simms_by_country = df_simms_by_country.rename(columns={'Ma':'Marilyns', 'Hu':'HuMPS', 'Sim':'Simms'})

print()
print('Mountain Types by Country')
print(df_simms_by_country)
print()

# Calculate highest mountains
df_highest = df.sort_values('Metres', ascending=False).head(10).reset_index(drop=True)
df_highest = df_highest[['Name', 'Metres', 'Country']]

print('Highest Mountains')
print(df_highest)
print()