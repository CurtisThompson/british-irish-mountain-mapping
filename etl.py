import pandas as pd


def etl():
    # Import data
    df = pd.read_csv('./data/hills.csv')

    # Keep only required columns for calculations
    cols_to_keep = ['Number', 'Name', 'Parent (SMC)', 'County', 'Metres', 'Drop', 'Latitude', 'Longitude',
                    'Ma', 'Hu', 'Sim', 'M', 'MT', 'F']
    df = df[cols_to_keep]

    # Flag for P600 mountains (drop above 600m)
    df['P600'] = df['Drop'] > 600
    df['P600'] = df['P600'].astype(int)

    # Map counties to countries of UK
    county_map = pd.read_csv('./data/county_mapping.csv').set_index('County').to_dict()['Country']
    df['FirstCounty'] = df['County'].apply(lambda x: x.split('/')[0])
    df['Country'] = df['FirstCounty'].map(county_map)

    # Add description column
    df['KMLDesc'] = df.apply(lambda x: f'Height of{x.Metres}m. Prominence of {x.Drop}m.', axis=1)

    # Filter out everything that is not a Marilyn, HuMP, Simm, Munro, or Furth
    # Marilyn: Drop above 150m
    # HuMP: Drop above 100m
    # Simm: Height above 600m and drop above 30m
    # Munro: Scottish mountains with height above 914.4m (3000ft) with no parent
    # Furths: Mountains outside of Scotland that would otherwise qualify as Munro
    df = df[df.Ma + df.Hu + df.Sim + df.M + df.MT + df.F + df.P600 > 0]

    # Save to file
    df.to_csv('./data/hills_etl.csv', index=False)


if __name__ == "__main__":
    etl()