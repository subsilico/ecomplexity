import subprocess
import os

def install_trivy():
    # Check if Trivy is already installed
    try:
        subprocess.run(["trivy", "--version"], check=True)
        print("Trivy is already installed.")
    except:
        # Trivy is not installed, download and install it
        print("Installing Trivy...")
        os.system("wget https://github.com/aquasecurity/trivy/releases/download/v0.47.0/trivy_0.47.0_Linux-64bit.tar.gz")
        os.system("tar zxvf trivy_0.47.0_Linux-64bit.tar.gz")
        os.system("sudo mv trivy /usr/local/bin/")
        #os.system("rm trivy_0.19.0_Linux-64bit.tar.gz")
        print("Trivy installed successfully.")

def scan_and_inspect(image_name):
    try:
        # Run Trivy to scan the Docker image
        scan_result = subprocess.run(
            ["trivy", "image", "--ignore-unfixed", image_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Print the scan results
        print(scan_result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error inspecting vulnerabilities: {e}")
        print(e.stderr)

if __name__ == "__main__":
    image_name = "my-app:latest"  # Replace with your Docker image name and tag

    # Install Trivy if not already installed
    install_trivy()

    # Scan and inspect the Docker image for vulnerabilities
    scan_and_inspect(image_name)

