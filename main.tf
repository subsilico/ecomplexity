
# main.tf

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13"  # Specify a suitable version
    }
  }
}

# Configure the Docker provider
provider "docker" {}

# Define a Docker image
resource "docker_image" "myapp" {
  name = "my-app:latest" # Replace with your image
}

# Run a Docker container
resource "docker_container" "myapp" {
  image = docker_image.myapp.latest
  name  = "myapp"
  ports {
    internal = 8000
    external = 8000
  }
}

