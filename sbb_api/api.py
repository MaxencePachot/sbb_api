import requests

def get_data(url: str, params: dict = None) -> dict:
    """Retrieves data from an API and
    returns a Python dictionary"""
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
