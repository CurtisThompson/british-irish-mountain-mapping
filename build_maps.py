import pandas as pd


def generate_placemark_kml(name, desc, lat, lon):
    """Creates a KML Placemark string."""
    return f'''    <Placemark>
        <name>{name}</name>
        <description>{desc}</description>
        <Point>
            <coordinates>{lon},{lat}</coordinates>
        </Point>
    </Placemark>\n'''


def dataframe_to_kml(df, name_col, desc_col, lat_col, lon_col):
    """Convert a DataFrame into a KML file."""
    text = '<?xml version="1.0" encoding="UTF-8"?>\n'
    text += '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    text += '<Document>\n'
    for index, row in df.iterrows():
        text += generate_placemark_kml(row[name_col],
                                       row[desc_col],
                                       row[lat_col],
                                       row[lon_col])
    text += '</Document>\n'
    text += '</kml>'
    return text


def hills_csv_to_kml():
    """Create KML documents for Marilyns and Simms."""
    df = pd.read_csv('./data/hills_etl.csv')

    # Create Marilyn KML
    df_m = df.loc[df.Ma == 1]
    kml = dataframe_to_kml(df_m, 'Name', 'KMLDesc', 'Latitude', 'Longitude')
    with open('./data/hills_marilyn.kml', 'w') as f:
        f.write(kml)
    
    # Create Simm KML
    df_s = df.loc[df.Sim == 1]
    kml = dataframe_to_kml(df_s, 'Name', 'KMLDesc', 'Latitude', 'Longitude')
    with open('./data/hills_simm.kml', 'w') as f:
        f.write(kml)
    
    # Create Simm KML
    df_se = df.loc[(df.Sim == 1) & (df.Country == 'England')]
    kml = dataframe_to_kml(df_se, 'Name', 'KMLDesc', 'Latitude', 'Longitude')
    with open('./data/hills_simm_england.kml', 'w') as f:
        f.write(kml)


#print(generate_placemark_kml('Mt', 'Big Mountain', 25, 30))
hills_csv_to_kml()