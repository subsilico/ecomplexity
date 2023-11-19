import docker

# Initialize the Docker client
client = docker.from_env()

def run_diagnostics():
    # Run known diagnostic functions
    try:
        # List containers
        containers = client.containers.list(all=True)
        print("List of containers:")
        for container in containers:
            print(f"Container ID: {container.id}, Name: {container.name}")

        # List images
        images = client.images.list()
        print("\nList of images:")
        for image in images:
            print(f"Image ID: {image.id}, Tags: {image.tags}")

        # Display Docker version information
        version_info = client.version()
        print("\nDocker version information:")
        print(f"Version: {version_info['Version']}, API version: {version_info['ApiVersion']}")

        # Offer initial advice
        print("\nInitial advice: Make sure your Dockerfile is properly configured and ready to build.")

    except docker.errors.APIError as e:
        print(f"Error running diagnostics: {e}")

if __name__ == "__main__":
    run_diagnostics()
