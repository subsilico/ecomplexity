import cython
import numpy as np
cimport numpy as cnp
from scipy.interpolate import UnivariateSpline
from numpy.random import choice
import multiprocessing

# C-level class for Cython methods
cdef class _MonteCarloHelper:
    def batch_calculate_epsilon_complexity(self, cnp.ndarray[double, ndim=2] data, int sample_size, int num_iterations):
        cdef int i
        cdef cnp.ndarray[double, ndim=2] all_sampled_data

        # Generate all samples for the given size at once
        for i in range(num_iterations):
            sampled_data = self.sample_data(data, sample_size)
            all_sampled_data = np.vstack([all_sampled_data, sampled_data]) if i > 0 else sampled_data

        # Spline fitting on the entire batch
        all_sampled_data = np.sort(all_sampled_data, axis=0)
        spline_fit = UnivariateSpline(all_sampled_data[:, 0], all_sampled_data[:, 1], s=0)

        # Calculate deviation for each sample in the batch
        cdef double total_deviation = 0
        for i in range(num_iterations):
            start_idx = i * sample_size
            end_idx = start_idx + sample_size
            approx_y = spline_fit(data[start_idx:end_idx, 0])
            total_deviation += np.mean((data[start_idx:end_idx, 1] - approx_y)**2)

        # Return average deviation
        return total_deviation / num_iterations

    def sample_data(self, cnp.ndarray[double, ndim=2] data, int sample_size):
        indices = choice(data.shape[0], sample_size, replace=False)
        return data[indices]

# Python class that users interact with
class MonteCarloSimulator:
    def __init__(self, int num_points, int num_sample_sizes, int num_iterations_per_size):
        self.helper = _MonteCarloHelper()
        self.num_points = num_points
        self.num_sample_sizes = num_sample_sizes
        self.num_iterations_per_size = num_iterations_per_size
        self.data = None

    def generate_cosine_data(self):
        cdef double[:] x = np.linspace(0, 2 * np.pi, self.num_points)
        cdef double[:] y = np.cos(x)
        self.data = np.vstack([x, y]).T

    def perform_monte_carlo_simulation_pooled(self):
        cdef int n = self.data.shape[0]
        cdef int[:] sample_sizes = np.round(np.linspace(n, 8, self.num_sample_sizes)).astype(np.int32)
        cdef double[:] results = np.zeros(self.num_sample_sizes, dtype=np.float64)

        # Define a function for parallel processing
        def calculate_for_sample_size(sample_size):
            return self.helper.batch_calculate_epsilon_complexity(self.data, sample_size, self.num_iterations_per_size)

        # Use multiprocessing to parallelize the loop
        with multiprocessing.Pool() as pool:
            results = pool.map(calculate_for_sample_size, sample_sizes)

        return results

    def perform_monte_carlo_simulation_sync(self):
        cdef int n = self.data.shape[0]
        cdef int[:] sample_sizes = np.round(np.linspace(n, 8, self.num_sample_sizes)).astype(np.int32)
        cdef double[:] results = np.zeros(self.num_sample_sizes, dtype=np.float64)

        cdef int j
        for j in range(self.num_sample_sizes):
            results[j] = self.helper.batch_calculate_epsilon_complexity(self.data, sample_sizes[j], self.num_iterations_per_size)

        return results
