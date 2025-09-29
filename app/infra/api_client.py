from dotenv import load_dotenv 

import os
import requests

load_dotenv()
API_URL = os.getenv('API_URL')

class APIClient:

    @staticmethod
    def get_users(params=None):
        endpoint = '/users'
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.get(url, params=params, headers=headers, timeout=1)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            return f'Erro ao conectar a API: {e}'
        
    @staticmethod
    def get_user_by_id(user_id):
        endpoint = f'/user/{user_id}'
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Erro ao conectar a API: {e}")
            return None
        
    @staticmethod
    def register(data):
        endpoint = '/register'
        url = f'{API_URL}{endpoint}'
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"Erro ao conectar a API: {e}")
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