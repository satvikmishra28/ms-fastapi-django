from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app) # r = requests.GET()

def test_get_home():
    response  = client.get("/") # request.get("") #python requests
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]

def test_post_home():
    response  = client.post("/")
    assert response.status_code == 200 #request.post("") #python requests
    assert "application/json" in response.headers["Content-Type"]
    assert response.json() =={"hello":"world"}
