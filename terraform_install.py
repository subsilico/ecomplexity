import subprocess
import os

def install_terraform():
    try:
        # Add HashiCorp GPG key
        subprocess.check_call("wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg", shell=True)

        # Add the HashiCorp Linux repository
        os_distribution = subprocess.check_output("lsb_release -cs", shell=True).strip().decode()
        repo_string = f"deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com {os_distribution} main"
        subprocess.check_call(f'echo "{repo_string}" | sudo tee /etc/apt/sources.list.d/hashicorp.list', shell=True)

        # Update and install Terraform
        subprocess.check_call("sudo apt update && sudo apt install terraform", shell=True)

        print("Terraform installed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_terraform()

