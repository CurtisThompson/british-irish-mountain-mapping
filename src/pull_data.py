import os
import requests
import zipfile
import shutil


def download_dobih_data():
    """Download Database of British and Irish Hills as csv to ./data/hills.csv."""
    # Create data directory if does not exist
    if not os.path.exists('./data'):
        os.mkdir('./data/')

    # Download the csv of hills
    url = 'http://www.hills-database.co.uk/hillcsv.zip'
    file_contents = requests.get(url, allow_redirects=True)
    open('./data/hills.zip', 'wb').write(file_contents.content)

    # Unzip downloaded file
    with zipfile.ZipFile('./data/hills.zip', 'r') as zip_ref:
        zip_ref.extractall('./data/')

    # Get csv name (most recently modified csv as just downloaded)
    files = [os.path.join('./data/', f) for f in os.listdir('./data/') if f.endswith('.csv')]
    files.sort(key=os.path.getmtime)
    csv_name = files[-1]

    # Copy file to a predetermined named file
    shutil.copy(csv_name, './data/hills.csv')

    # Remove any zip files
    zips = [os.path.join('./data/', f) for f in os.listdir('./data/') if f.endswith('.zip')]
    for zip in zips:
        os.remove(zip)


if __name__ == "__main__":
    download_dobih_data()