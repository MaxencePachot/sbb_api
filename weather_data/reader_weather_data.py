from adls_connection import get_adls_client
import pandas as pd
from io import BytesIO

def print_csv_from_adls(adls_folder: str, filename: str):
    """
    Download a CSV file from ADLS and display its contents as a pandas DataFrame
    """
    _, fs_client = get_adls_client()
    adls_path = f"{adls_folder}/{filename}"
    file_client = fs_client.get_file_client(adls_path)

    download = file_client.download_file()
    content = download.readall() # Give a bytes file so we have to convert it after

    df = pd.read_csv(BytesIO(content), sep=";") # Convert in csv
    
    # Display parameters
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    pd.set_option("display.max_colwidth", 10)

    print(f"Top 5 data in {filename} :")
    print(df.head(5))