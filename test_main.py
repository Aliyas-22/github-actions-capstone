from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

# ── root endpoint ──────────────────────────────────────

def test_root_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_root_message():
    response = client.get("/")
    assert response.json() == {"message": "welcome to api learning Aliya"}

# ── metrics endpoint ───────────────────────────────────

def test_metrics_status_code():
    response = client.get("/metrics")
    assert response.status_code == 200

def test_metrics_has_cpu():
    response = client.get("/metrics")
    assert "cpu_percentage" in response.json()

def test_metrics_has_memory():
    response = client.get("/metrics")
    assert "menmory_percentage" in response.json()

def test_metrics_has_disk():
    response = client.get("/metrics")
    assert "disk_percentage" in response.json()

def test_metrics_has_system_health():
    response = client.get("/metrics")
    assert "system_health" in response.json()

def test_metrics_cpu_threshold():
    response = client.get("/metrics")
    assert response.json()["cpu_threshold"] == 10

def test_metrics_health_value():
    response = client.get("/metrics")
    health = response.json()["system_health"]
    assert health in ["healthy", "High CPU Usage"]