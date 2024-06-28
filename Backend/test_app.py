import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_valid_url():
    response = client.post("/analyze", json={"url": "https://github.com/login"})
    assert response.status_code == 200
    data = response.json()
    assert "html_version" in data
    assert "title" in data
    assert "headings" in data
    assert "internal_links" in data
    assert "external_links" in data
    assert "login_form" in data
    assert "internal_links_validation" in data
    assert "external_links_validation" in data

def test_analyze_invalid_url():
    response = client.post("/analyze", json={"url": "invalid-url"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid URL 'invalid-url': No schema supplied. Perhaps you meant http://invalid-url?"}

def test_analyze_not_found_url():
    response = client.post("/analyze", json={"url": "https://github.com/login/404"})
    assert response.status_code == 400
    assert response.json() == {"detail": "404 Client Error: Not Found for url: https://github.com/login/404"}
