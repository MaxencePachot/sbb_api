import json
from adls_connection import get_adls_client

def upload_to_adls(path: str, data: dict, overwrite=True):
    """Upload a Python dictionary in JSON format to ADLS"""
    _, file_system_client = get_adls_client()
    file_client = file_system_client.get_file_client(path)

    file_contents = json.dumps(data, indent=2)
    file_client.upload_data(file_contents, overwrite=overwrite)
    print(f"Data uploaded successfully to {path}!")
