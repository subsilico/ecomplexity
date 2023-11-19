import subprocess

def apply_terraform():
    try:
        # Running Terraform apply
        subprocess.check_call(["terraform", "apply", "-auto-approve"], cwd='.')
        print("Terraform apply executed successfully.")

    except subprocess.CalledProcessError as e:
        print("An error occurred during Terraform apply:", e)

if __name__ == "__main__":
    apply_terraform()

