import os
from adls_connection import get_adls_client

def upload_csv_folder_to_adls(local_folder: str, adls_folder: str):
    """
    Upload all CSV files from a local folder to ADLS in a target folder.
    Existing files with the same name will be overwritten.
    """
    _, file_system_client = get_adls_client()

    for filename in os.listdir(local_folder):
        if filename.endswith(".csv"):
            local_path = os.path.join(local_folder, filename)

            with open(local_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            adls_path = f"{adls_folder}/{filename}"

            file_client = file_system_client.get_file_client(adls_path)
            file_client.upload_data(content, overwrite=True)
            print(f"{filename} uploaded to ADLS at {adls_path}")
