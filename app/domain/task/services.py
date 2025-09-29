import requests

from app.infra.api_client import APIClient

class TaskService():

    @staticmethod
    def create_task(form):
        data = {
            'title': form.title.data,
            'description': form.description.data
        }

        try:
            response_api = APIClient.create_task(data)
            return response_api
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão com a API: {e}")
            return None
    