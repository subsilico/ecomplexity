# Use an official R runtime as a parent image
FROM r-base

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Update the machine 
RUN apt-get update -qq && apt-get install -y \
  libssl-dev \
  libcurl4-gnutls-dev

# Do the librarys needed. These are for plumber
RUN apt install -y libsodium-dev

# Install any needed packages specified in requirements.txt
# RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('plumber')"

# Let through web traffic to the service
EXPOSE 8000

# Run app.R from the plumber.R when the container launches
CMD ["Rscript", "plumber.R"]

