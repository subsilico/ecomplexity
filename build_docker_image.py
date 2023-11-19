import subprocess

def build_docker_image(image_name, dockerfile_path):
    try:
        subprocess.run(["docker", "build", "-t", image_name, dockerfile_path], check=True)
        print(f"Successfully built Docker image: {image_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e}")

if __name__ == "__main__":
    image_name = "my-app:latest"  # Replace with your desired image name and tag
    dockerfile_path = "."  # Replace with the path to your Dockerfile
    build_docker_image(image_name, dockerfile_path)

