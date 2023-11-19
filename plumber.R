library(plumber);

pr <- plumber::plumb('app.R');

#pr$run(port=8000, host="0.0.0.0")
pr$run(port=8000, host="0.0.0.0")
