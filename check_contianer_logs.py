import subprocess

def check_container_logs(container_name):
    try:
        subprocess.run(["docker", "logs", container_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error checking container logs: {e}")

if __name__ == "__main__":
    container_name = "my-app-container"  # Replace with your container name
    check_container_logs(container_name)

