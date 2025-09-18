from infra.api_client import APIClient

class UserRepository():

    def find_all():
        return APIClient.get("/users")

    def find_by_id(user_id: int):
        return APIClient.get(f"user/{user_id}")

    def create_user(data: dict):
        return APIClient.post("/user", data=data)

    def update(user_id: int):
        return APIClient.put(f"/user/{user_id}")

    def delete(user_id: int):
        return APIClient.delete(f"/user/{user_id}")