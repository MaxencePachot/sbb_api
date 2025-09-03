import argparse
from sbb_api.api import get_data
from sbb_api.storage_sbb_data import upload_to_adls
from sbb_api.reader_sbb_data import print_from_adls
from weather_data.upload_weather_data import upload_csv_folder_to_adls
from weather_data.reader_weather_data import print_csv_from_adls

def main():
    # Arguments (more flexibility)
    parser = argparse.ArgumentParser(description="Run retrieval of data steps")
    parser.add_argument("--upload_sbb", action="store_true", help="Upload SBB JSON data to ADLS")
    parser.add_argument("--upload_csv", action="store_true", help="Upload all CSV weather data to ADLS")
    parser.add_argument("--read", action="store_true", help="Read JSON from ADLS")
    parser.add_argument("--read_csv", action="store_true", help="Read a weather CSV from ADLS")
    parser.add_argument("--csv_file", type=str, help="Name of the CSV file to read")
    args = parser.parse_args()
    
    # Parameters
    sbb_url = "https://data.sbb.ch/api/explore/v2.1/catalog/datasets/ist-daten-sbb/records"
    json_path = "data/sbb.json"
    csv_local_folder = "data"
    csv_adls_folder = "data"

    # Upload data from sbb api in adls
    if args.upload_sbb:
        data = get_data(sbb_url)
        upload_to_adls(json_path, data)

    # Read json from sbb data in adls
    if args.read:
        print_from_adls(json_path)

    # Upload csv in adls
    if args.upload_csv:
        upload_csv_folder_to_adls(csv_local_folder, csv_adls_folder)

    # Read csv in adls
    if args.read_csv:
        if args.csv_file:
            print_csv_from_adls(csv_adls_folder, args.csv_file)
        else:
            print("Please specify the name of the CSV file to be read with --csv_file")
            
if __name__ == "__main__":
    main()
