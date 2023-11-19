import requests
import numpy as np

def generate_cosine_data(n):
    x = np.linspace(0, 2 * np.pi, n)
    y = np.cos(x)
    return [{"x": float(x_val), "y": float(y_val)} for x_val, y_val in zip(x, y)]

def test_monte_carlo_service(url, data, num_sample_sizes, num_iterations_per_size):
    payload = {
        "data": data,
        "numSampleSizes": num_sample_sizes,
        "numIterationsPerSize": num_iterations_per_size
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Success! Response from Monte Carlo service:")
        print(response.json())
    else:
        print(f"Failed to get a successful response from Monte Carlo service. Status Code: {response.status_code}")
        print("Response:", response.text)

def test_echo_service(url, message):
    response = requests.get(url, params={"msg": message})
    if response.status_code == 200:
        print("Success! Response from Echo service:")
        print(response.json())
    else:
        print(f"Failed to get a successful response from Echo service. Status Code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    montecarlo_service_url = "http://localhost:8000/montecarlo"
    echo_service_url = "http://localhost:8000/echo"
    
    # Test /montecarlo endpoint
    sample_data = generate_cosine_data(100)  # Generate 100 data points
    num_sample_sizes = 5
    num_iterations_per_size = 10
    test_monte_carlo_service(montecarlo_service_url, sample_data, num_sample_sizes, num_iterations_per_size)

    # Test /echo endpoint
    test_echo_service(echo_service_url, "Hello")

