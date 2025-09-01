from sbb_api.api import get_data
from sbb_api.storage import upload_to_adls
from sbb_api.reader import print_from_adls

def main():
    url = "https://data.sbb.ch/api/explore/v2.1/catalog/datasets/ist-daten-sbb/records?limit=1"
    data = get_data(url)

    path = "data/output.json"
    upload_to_adls(path, data)

    print_from_adls(path)

if __name__ == "__main__":
    main()
