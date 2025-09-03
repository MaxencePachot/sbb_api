from azure.storage.filedatalake import DataLakeServiceClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_adls_client():
    """Returns a client service and client file system for ADLS"""
    account_url = os.getenv("STORAGE_ACCOUNT_URL")
    credential = os.getenv("STORAGE_ACCOUNT_KEY")
    filesystem = os.getenv("FILESYSTEM")

    service_client = DataLakeServiceClient(account_url=account_url, credential=credential)
    file_system_client = service_client.get_file_system_client(filesystem)
    return service_client, file_system_client