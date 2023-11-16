import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

def generate_cosine_data(n):
    x = np.linspace(0, 2 * np.pi, n)
    y = np.cos(x)
    return pd.DataFrame({'x': x, 'y': y})

def generate_sine_data(n):
    x = np.linspace(0, 2 * np.pi, n)
    y = np.sin(x)
    return pd.DataFrame({'x': x, 'y': y})

def generate_uniform_random_data(n):
    x = np.linspace(0, 1, n)
    y = np.random.uniform(size=n)
    return pd.DataFrame({'x': x, 'y': y})

def perform_monte_carlo_simulation(data, num_sample_sizes, num_iterations_per_size):
    n = len(data)
    sample_sizes = np.round(np.linspace(n, 8, num_sample_sizes)).astype(int)
    results = []

    for sample_size in sample_sizes:
        complexity_sum = 0
        for _ in range(num_iterations_per_size):
            sampled_data = data.sample(sample_size)
            complexity_sum += calculate_epsilon_complexity(sampled_data, data)
        
        results.append(complexity_sum / num_iterations_per_size)

    return pd.DataFrame({'sample_sizes': sample_sizes, 'complexity': results})

def calculate_epsilon_complexity(sampled_data, original_data):
    # Sort the sampled data to ensure x values are in increasing order
    sampled_data_sorted = sampled_data.sort_values(by='x')

    spline_fit = UnivariateSpline(sampled_data_sorted['x'], sampled_data_sorted['y'], s=0)
    approx_y = spline_fit(original_data['x'])
    deviation = np.mean((original_data['y'] - approx_y)**2)
    return deviation


def generate_cosine_data(n):
    x = np.linspace(0, 2 * np.pi, n)
    y = np.cos(x)
    return pd.DataFrame({'x': x, 'y': y})

def generate_sine_data(n):
    x = np.linspace(0, 2 * np.pi, n)
    y = np.sin(x)
    return pd.DataFrame({'x': x, 'y': y})

def generate_uniform_random_data(n):
    x = np.linspace(0, 1, n)
    y = np.random.uniform(size=n)
    return pd.DataFrame({'x': x, 'y': y})

# Generate the data
num_points = 50
cosData = generate_cosine_data(num_points)
sineData = generate_sine_data(num_points)
uniformData = generate_uniform_random_data(num_points)



# Assuming you have already generated the data using the functions above

# Cosine Data Plot
plt.figure()
plt.plot(cosData['x'], cosData['y'], color='blue')
plt.title('Cosine Function Data')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.savefig('cosine_data_plot.png')  # Saving the plot

# Sine Data Plot
plt.figure()
plt.plot(sineData['x'], sineData['y'], color='green')
plt.title('Sine Function Data')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.savefig('sine_data_plot.png')  # Saving the plot

# Uniform Random Data Plot
plt.figure()
plt.plot(uniformData['x'], uniformData['y'], color='red')
plt.title('Uniform Random Data')
plt.xlabel('x')
plt.ylabel('Uniform Random Values')
plt.savefig('uniform_random_data_plot.png')  # Saving the plot


# Parameters for the simulation
num_sample_sizes = 20  # Number of different sample sizes to test
num_iterations_per_size = 100  # Number of iterations per sample size

# Running the simulation for cosine data
cosResults = perform_monte_carlo_simulation(cosData, num_sample_sizes, num_iterations_per_size)

# Running the simulation for sine data
sineResults = perform_monte_carlo_simulation(sineData, num_sample_sizes, num_iterations_per_size)

# Running the simulation for uniform random data
uniformResults = perform_monte_carlo_simulation(uniformData, num_sample_sizes, num_iterations_per_size)


# Assuming cosResults, sineResults, uniformResults are obtained from the simulations

# Preparing data for plotting
cos_complexity_df = pd.DataFrame({
    'SampleSize': cosResults['sample_sizes'],
    'EpsilonComplexity': cosResults['complexity'],
    'Dataset': 'Cosine'
})

sine_complexity_df = pd.DataFrame({
    'SampleSize': sineResults['sample_sizes'],
    'EpsilonComplexity': sineResults['complexity'],
    'Dataset': 'Sine'
})

uniform_complexity_df = pd.DataFrame({
    'SampleSize': uniformResults['sample_sizes'],
    'EpsilonComplexity': uniformResults['complexity'],
    'Dataset': 'Uniform Random'
})

complexity_df = pd.concat([cos_complexity_df, sine_complexity_df, uniform_complexity_df])

# Plotting the results
plt.figure()
for label, df in complexity_df.groupby('Dataset'):
    plt.plot(df['SampleSize'], df['EpsilonComplexity'], marker='o', label=label)

plt.title('Epsilon Complexity vs Sample Size')
plt.xlabel('Sample Size')
plt.ylabel('Epsilon Complexity')
plt.legend()
plt.savefig('epsilon_complexity_plot.png')  # Saving the plot
