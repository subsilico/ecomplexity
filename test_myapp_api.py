import requests
import numpy as np
import pytest

def generate_cosine_data(n):
    x = np.linspace(0, 2 * np.pi, n)
    y = np.cos(x)
    return [{"x": float(x_val), "y": float(y_val)} for x_val, y_val in zip(x, y)]

@pytest.fixture
def montecarlo_url():
    return "http://localhost:8000/montecarlo"

@pytest.fixture
def echo_url():
    return "http://localhost:8000/echo"

def test_echo_service(echo_url):
    response = requests.get(echo_url, params={"msg": "Hello"})
    assert response.status_code == 200
    assert response.json() == {"msg": ["The message is: 'Hello'\n"]}

def test_monte_carlo_service(montecarlo_url):
    sample_data = generate_cosine_data(100)  # Generate 100 data points
    payload = {
        "data": sample_data,
        "numSampleSizes": 5,
        "numIterationsPerSize": 10
    }
    
    response = requests.post(montecarlo_url, json=payload)
    assert response.status_code == 200
    # Additional assertions can be added here to validate the response content


