import subprocess

def check_terraform_installation():
    try:
        # Check if Terraform is installed and get its version
        terraform_version = subprocess.check_output(["terraform", "-v"], text=True)
        print("Terraform is installed.")
        print("Version information:\n", terraform_version)

    except subprocess.CalledProcessError:
        print("Terraform is not installed or not found in PATH.")

if __name__ == "__main__":
    check_terraform_installation()

