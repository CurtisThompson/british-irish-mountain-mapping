import pandas as pd


def show_stats():
    # Load processed data
    df = pd.read_csv('./data/hills_etl.csv')

    # Get total mountain types
    df_simms = df.sum()[['Ma', 'Hu', 'Sim', 'P600']]

    print()
    print('Mountain Types')
    print(df_simms)
    print()

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


if __name__ == "__main__":
    show_stats()