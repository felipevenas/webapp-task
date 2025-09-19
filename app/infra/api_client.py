from dotenv import load_dotenv 

import os
import requests

load_dotenv()
API_URL = os.getenv('API_URL')

class APIClient:

    @staticmethod
    def _request(method, endpoint, data=None, params=None):
        url = f"{API_URL}/{endpoint}"
        try:
            response = requests.request(method, url, json=data, params=params, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 204:
                return None
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro de comunicação com a API em {method} {url}: {e}")        

    @staticmethod
    def get(endpoint, params=None):
        return APIClient._request('GET', endpoint, params=params)
    
    @staticmethod
    def post(endpoint, data=None):
        return APIClient._request('POST', endpoint, data=data)
    
    @staticmethod
    def put(endpoint, data=None):
        return APIClient._request('PUT', endpoint, data=data)
    
    @staticmethod
    def delete(endpoint, data=None):
        return APIClient._request('DELETE', endpoint, data=data)