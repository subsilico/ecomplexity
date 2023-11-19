import subprocess

def get_docker_image_history(image_name):
    try:
        result = subprocess.run(["docker", "history", image_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    image_name = "my-app:latest"  # Replace with your Docker image name
    get_docker_image_history(image_name)

