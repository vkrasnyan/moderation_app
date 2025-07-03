from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_moderate_endpoint():
    with open("test_image.jpg", "rb") as img:
        response = client.post("/moderate", files={"file": ("test_image.jpg", img, "image/jpeg")})

    assert response.status_code == 200
    assert response.json()["status"] in ["OK", "REJECTED"]
