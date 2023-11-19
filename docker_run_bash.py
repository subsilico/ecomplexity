import subprocess

def run_docker_container_interactively(image_tag):
    try:
        subprocess.run(["docker", "run", "-it", "--entrypoint", "/bin/bash", image_tag])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    image_tag = "my-app:latest"  # Replace with your Docker image tag
    run_docker_container_interactively(image_tag)

