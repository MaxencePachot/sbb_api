import json
from .adls_connection import get_adls_client

def read_from_adls(path: str) -> dict:
    """Reads a JSON file from ADLS and returns a Python dictionary"""
    _, file_system_client = get_adls_client()
    file_client = file_system_client.get_file_client(path)

    download = file_client.download_file()
    file_contents = download.readall()
    data = json.loads(file_contents)
    return data

def print_from_adls(path: str):
    """Print the contents of the JSON file from ADLS"""
    data = read_from_adls(path)
    print(json.dumps(data, indent=2))
