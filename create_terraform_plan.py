import subprocess

def create_terraform_plan():
    try:
        # Generate Terraform plan
        subprocess.check_call(["terraform", "plan"], cwd='.')
        print("Terraform plan created successfully.")

    except subprocess.CalledProcessError as e:
        print("An error occurred while creating the Terraform plan:", e)

if __name__ == "__main__":
    create_terraform_plan()

