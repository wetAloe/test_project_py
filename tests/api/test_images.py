import pytest
from fastapi.testclient import TestClient
from fastapi import status


@pytest.fixture
def image_data() -> list[int]:
    return [0] * 200


def test_create_image(client: TestClient, image_data: list[int]):
    response = client.post("/images/", json={"data": image_data})
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    assert data["id"] == 1


def test_get_image(client: TestClient, image_data: list[int]):
    # First create an image
    response = client.post("/images/", json={"data": image_data})
    image_id = response.json()["id"]
    assert image_id == 1

    # Then retrieve it
    response = client.get(f"/images/{image_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == image_id


def test_delete_image(client: TestClient, image_data: list[int]):
    # First create an image
    response = client.post("/images/", json={"data": image_data})
    image_id = response.json()["id"]
    assert image_id == 1

    # Then delete it
    response = client.delete(f"/images/{image_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify it's gone
    response = client.get(f"/images/{image_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_images_range(client: TestClient, image_data: list[int]):
    # Create a few images
    for _ in range(3):
        client.post("/images/", json={"data": image_data})

    # Get range of images
    response = client.get("/images/?min_depth=1&max_depth=3")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 3
