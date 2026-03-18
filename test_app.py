import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_health_check(client):
    """Test if the health endpoint returns 200 OK and correct JSON"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy", "version": "1.0.0"}
