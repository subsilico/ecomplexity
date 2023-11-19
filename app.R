# app.R

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

#* Echo back the input
#* @param msg The message to echo back.
#* @get /echo
function(msg="") {
  list(msg = paste0("The message is: '", msg, "'\n"))
}

#* Perform Monte Carlo simulation
#* @post /montecarlo
function(req) {
  params <- jsonlite::fromJSON(req$postBody)
  data <- params$data
  numSampleSizes <- params$numSampleSizes
  numIterationsPerSize <- params$numIterationsPerSize

  performMonteCarloSimulation(data, numSampleSizes, numIterationsPerSize)
}

