# Epsilon-Complexity : Paramaterize Timeseries and Timeseries-like Data

See https://arxiv.org/abs/1303.1777

![The curve genrated by the code](https://raw.githubusercontent.com/subsilico/ecomplexity/main/ecomplexitycurve.png)

Shown is an example of how sine and cosine have the same e-complexity while random data is much different. (See how blue's basal error is increased?) All that is left is parameterizing the curves to create a parameter hyperspace for your timeseries/timeseries-like data. 

On offer are: 
1) R-Project Markdown version of the code that is very slow but easy to understand,
2) Python implementation that can be used easily,
3) Cython routines for speedy monte-carlo simulations.

What is left to the user is converting the epsilon-complexity results into a set of parameters via line fitting. Current research suggests that at least four parameters are needed to achieve a good fit.

# The R markdown

## Introduction

This document presents an analysis of the epsilon-complexity of time series data using Monte Carlo simulations and cubic spline interpolation. We'll focus on two cases: a cosine function and a uniform random distribution.

## Setup

Load necessary libraries and define our data generation and analysis functions.

```{r setup}
library(splines)

generateCosineData <- function(n) {
  x <- seq(0, 2*pi, length.out = n)
  y <- cos(x)
  return(data.frame(x, y))
}

generateSineData <- function(n) {
  x <- seq(0, 2*pi, length.out = n)
  y <- sin(x)
  return(data.frame(x, y))
}

generateUniformRandomData <- function(n) {
  x <- seq(0, 1, length.out = n)
  y <- runif(n)
  return(data.frame(x, y))
}

performMonteCarloSimulation <- function(data, numSampleSizes, numIterationsPerSize) {
  n <- nrow(data)
  # Ensure minimum sample size is 4 for smooth.spline to work
  sampleSizes <- round(seq(n, 4, length.out = numSampleSizes))
  results <- numeric(length(sampleSizes))

  for (j in seq_along(sampleSizes)) {
    sampleSize <- sampleSizes[j]
    complexitySum <- 0

    for (i in 1:numIterationsPerSize) {
      sampledData <- data[sample(1:n, sampleSize), ]
      complexitySum <- complexitySum + calculateEpsilonComplexity(sampledData, data)
    }

    results[j] <- complexitySum / numIterationsPerSize
  }

  return(list(sampleSizes = sampleSizes, complexity = results))
}

calculateEpsilonComplexity <- function(sampledData, originalData) {
  splineFit <- smooth.spline(sampledData$x, sampledData$y)
  approxData <- predict(splineFit, originalData$x)
  deviation <- mean((originalData$y - approxData$y)^2)
  return(deviation)
}
```

## Generate Sample Function
```{r generate}
numPoints <- 50
cosData <- generateCosineData(numPoints)
sineData <- generateSineData(numPoints)
uniformData <- generateUniformRandomData(numPoints)
```

```{r run-simulation}
# Parameters for the simulation
numSampleSizes <- 20 # Number of different sample sizes to test
numIterationsPerSize <- 100 # Number of iterations per sample size

# Running the simulation for cosine data
cosResults <- performMonteCarloSimulation(cosData, numSampleSizes, numIterationsPerSize)

# Running the simulation for sine data
sineResults <- performMonteCarloSimulation(sineData, numSampleSizes, numIterationsPerSize)

# Running the simulation for uniform random data
uniformResults <- performMonteCarloSimulation(uniformData, numSampleSizes, numIterationsPerSize)
```

## Plotting Synthetic Data

Visualizing the generated time series data for both the cosine function and uniform random distribution.

```{r plot-synthetic-data}
library(ggplot2)

# Cosine Data Plot
ggplot(cosData, aes(x = x, y = y)) +
  geom_line(color = 'blue') +
  ggtitle('Cosine Function Data') +
  xlab('x') +
  ylab('cos(x)')

# Uniform Random Data Plot
ggplot(uniformData, aes(x = x, y = y)) +
  geom_line(color = 'red') +
  ggtitle('Uniform Random Data') +
  xlab('x') +
  ylab('Uniform Random Values')

ggplot(sineData, aes(x = x, y = y)) +
  geom_line(color = 'green') +
  ggtitle('Sine Function Data') +
  xlab('x') +
  ylab('sin(x)')

```



## Show results from the simulation

```{r}
# Epsilon Complexity for Cosine Data
print('Epsilon Complexity for Cosine Data:')
print(cosResults)

# Epsilon Complexity for Sine Data
print('Epsilon Complexity for Sine Data:')
print(sineResults)

# Epsilon Complexity for Uniform Random Data
print('Epsilon Complexity for Uniform Random Data:')
print(uniformResults)
```

## Plotting Epsilon Complexity Results

Visualizing the change in epsilon complexity with different sample sizes for both the cosine function and uniform random distribution.

```{r plot-epsilon-complexity}
library(ggplot2)

# Preparing data for plotting
cos_complexity_df <- data.frame(SampleSize = cosResults$sampleSizes, 
                                EpsilonComplexity = cosResults$complexity, 
                                Dataset = 'Cosine')
sine_complexity_df <- data.frame(SampleSize = sineResults$sampleSizes, 
                                 EpsilonComplexity = sineResults$complexity, 
                                 Dataset = 'Sine')
uniform_complexity_df <- data.frame(SampleSize = uniformResults$sampleSizes, 
                                    EpsilonComplexity = uniformResults$complexity, 
                                    Dataset = 'Uniform Random')
complexity_df <- rbind(cos_complexity_df, uniform_complexity_df, sine_complexity_df)


# Plotting the results
ggplot(complexity_df, aes(x = SampleSize, y = EpsilonComplexity, color = Dataset)) +
  geom_line() +
  geom_point() +
  theme_minimal() +
  ggtitle('Epsilon Complexity vs Sample Size') +
  xlab('Sample Size') +
  ylab('Epsilon Complexity')
```
