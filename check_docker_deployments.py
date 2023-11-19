import subprocess

def inspect_docker_deployment(container_name):
    try:
        # Inspect the Docker container
        container_details = subprocess.check_output(["docker", "inspect", container_name], text=True)
        print("Container Details:\n", container_details)

        # Check the status of the Docker container
        container_status = subprocess.check_output(["docker", "ps", "-f", f"name={container_name}"], text=True)
        print("Container Status:\n", container_status)

    except subprocess.CalledProcessError as e:
        print("An error occurred while inspecting the Docker deployment:", e)

if __name__ == "__main__":
    inspect_docker_deployment("myapp")  # Replace with your container name

