import allure
import pytest
import requests
from models import Pet

petstore_api_url = "https://petstore.swagger.io/v2/pet"

@allure.title("Create pet")
def test_create_pet():
    with allure.step("Step 1: Create pet"):
        pet_data = {
            "id": 1,
            "category": {"id": 1, "name": "dogs"},
            "name": "Buddy",
            "photoUrls": ["https://example.com/buddy.jpg"],
            "tags": [{"id": 1, "name": "friendly"}],
            "status": "available"
        }

        response = requests.post(petstore_api_url, json=pet_data)

    with allure.step("Step 2: Check status answer"):
        assert response.status_code == 200

@allure.title("Получение питомца по ID")
def test_get_pet_by_id():
    pet_id = 1

    with allure.step(f"Step 1: Receiving pet with ID {pet_id}"):
        response = requests.get(f"{petstore_api_url}/{pet_id}")

    with allure.step("Step 2: Check status answer"):
        assert response.status_code == 200
        pet = Pet(**response.json())
        assert pet.id == pet_id

@allure.title("Delete pet")
def test_delete_pet():
    pet_id = 1

    with allure.step(f"Step 1: Delete pet with ID {pet_id}"):
        response = requests.delete(f"{petstore_api_url}/{pet_id}")

    with allure.step("Step 2: Check status answer"):
        assert response.status_code == 200

@allure.title("Receiving list pet")
def test_get_all_pets():
    with allure.step("Step 1: Receiving list all pet"):
        response = requests.get(f"{petstore_api_url}/findByStatus?status=available")

    with allure.step("Step 2: Check status answer"):
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)