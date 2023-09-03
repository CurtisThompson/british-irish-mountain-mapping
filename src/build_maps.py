import os
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

    # KML files to create, tuple is file_name and DataFrame filter
    kml_groups = [('./data/kml/hills_marilyn.kml', df.Ma == 1),
                  ('./data/kml/hills_simm.kml', df.Sim == 1),
                  ('./data/kml/hills_simm_england.kml', (df.Sim == 1) & (df.Country == 'England'))]
    
    # Create KML file directory if does not exist
    if not os.path.exists('./data/kml/'):
        os.mkdir('./data/kml/')

    # Create each KML file
    for file_data in kml_groups:
        df_temp = df.loc[file_data[1]]
        kml = dataframe_to_kml(df_temp, 'Name', 'KMLDesc', 'Latitude', 'Longitude')
        with open(file_data[0], 'w') as f:
            f.write(kml)


if __name__ == "__main__":
    hills_csv_to_kml()