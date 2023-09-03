from src.pull_data import download_dobih_data
from src.etl import etl
from src.build_maps import hills_csv_to_kml
from src.build_figures_and_stats import show_stats


def run():
    download_dobih_data()
    etl()
    hills_csv_to_kml()
    show_stats()


if __name__ == "__main__":
    run()