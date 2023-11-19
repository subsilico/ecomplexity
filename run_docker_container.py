import subprocess

def run_docker_container(container_name, image_name):
    try:
        subprocess.run(["docker", "run", "-d", "--name", container_name, image_name], check=True)
        print(f"Successfully started Docker container: {container_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error starting Docker container: {e}")

if __name__ == "__main__":
    container_name = "my-app-container"  # Replace with your desired container name
    image_name = "my-app:latest"  # Replace with your Docker image name and tag
    run_docker_container(container_name, image_name)

