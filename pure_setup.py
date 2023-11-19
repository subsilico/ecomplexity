import subprocess

# Check if Docker is installed
def check_docker_installation():
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Install Docker SDK for Python using pip if not already installed
def install_docker_sdk():
    try:
        subprocess.run(["pip", "install", "docker"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error installing Docker SDK for Python: {e}")

def run_diagnostics():
    # Check if Docker is installed
    if not check_docker_installation():
        print("Docker is not installed. Please install Docker first.")
        return

    # Install Docker SDK for Python if not already installed
    try:
        import docker
    except ImportError:
        print("Docker SDK for Python is not installed. Installing...")
        install_docker_sdk()
        import docker

    # Initialize the Docker client
    client = docker.from_env()

    # Rest of the diagnostic and advice code remains the same
    # ...

if __name__ == "__main__":
    run_diagnostics()

