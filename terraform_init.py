import subprocess
import os

def init_terraform(directory):
    try:
        # Change to the desired directory
        os.chdir(directory)

        # Initialize Terraform in the directory
        subprocess.check_call(["terraform", "init"])
        print("Terraform has been successfully initialized in:", directory)

    except subprocess.CalledProcessError as e:
        print("An error occurred during Terraform initialization:", e)
    except FileNotFoundError:
        print(f"The directory {directory} was not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Replace with the path to your Terraform project directory
    terraform_project_dir = "."
    init_terraform(terraform_project_dir)

