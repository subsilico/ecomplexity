import subprocess
import sys

def run_command(command, check=True, capture_output=False):
    try:
        result = subprocess.run(command, check=check, stdout=subprocess.PIPE if capture_output else None)
        return result.stdout.decode('utf-8').strip() if capture_output else ""
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        if not check:
            return e.stdout.decode('utf-8').strip()
        sys.exit(1)

def is_package_installed(package):
    status = subprocess.run(["dpkg", "-s", package], stdout=subprocess.DEVNULL)
    return status.returncode == 0

def check_version(command):
    version = run_command(command, capture_output=True)
    print(f"{command[0]} version: {version}")

def check_process_running(process):
    result = run_command(["pgrep", "-f", process], check=False, capture_output=True)
    if result:
        print(f"{process} process is running.")
    else:
        print(f"{process} process is not running or not found.")


print("Checking if kubelet, kubeadm, and kubectl are installed...")
for package in ["kubelet", "kubeadm", "kubectl"]:
    if is_package_installed(package):
        print(f"{package} is installed successfully.")
    else:
        print(f"{package} is not installed.")

print("\nChecking versions of installed components...")
check_version(["kubelet", "--version"])
check_version(["kubeadm", "version"])
check_version(["kubectl", "version", "--client"])

print("\nChecking if the kubelet process is running...")
check_process_running("kubelet")

