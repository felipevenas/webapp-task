from dotenv import load_dotenv 

import os
import requests

load_dotenv()
API_URL = os.getenv('API_URL')

class APIClient:

    @staticmethod
    def create(endpoint, data):
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url=url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"Erro ao conectar a API: {e}")
            return None
    
    @staticmethod
    def get_all():
        endpoint = '/users'
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.get(url=url, headers=headers, timeout=1)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            return f'Erro ao conectar a API: {e}'
        
    @staticmethod
    def get_by_id(endpoint):
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.get(url=url, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        
        except requests.exceptions.HTTPError as e:
            print(f"Erro ao conectar a API: {e}")
            return None
        
    @staticmethod
    def delete(endpoint):
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.delete(url=url, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        
        except requests.exceptions.HTTPError as e:
            print(f'Erro ao conectar a API: {e}')
            return None

    @staticmethod
    def update(endpoint, data):
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.put(url=url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        
        except requests.exceptions.HTTPError as e:
            print(f'Erro ao conectar a API: {e}')
            return None

    @staticmethod
    def login(data):
        endpoint = '/auth'
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url=url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f'Erro ao conectar a API: {e}')
            return None
        