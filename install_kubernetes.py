import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def is_package_installed(package):
    status = subprocess.run(["dpkg", "-s", package], stdout=subprocess.DEVNULL)
    return status.returncode == 0

print("Updating package lists...")
run_command(["sudo", "apt-get", "update"])

print("Adding the Kubernetes signing key using os.system...")
os.system("sh -c 'curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -'")

print("Adding the specific public key for Kubernetes...")
run_command(["sudo", "apt-key", "adv", "--keyserver", "keyserver.ubuntu.com", "--recv-keys", "B53DC80D13EDEF05"])

print("Adding the Kubernetes repository...")
run_command(["sudo", "sh", "-c", 'echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list'])

print("Updating package lists again...")
run_command(["sudo", "apt-get", "update"])

print("Installing kubelet, kubeadm, and kubectl...")
run_command(["sudo", "apt-get", "install", "-y", "kubelet", "kubeadm", "kubectl"])

print("Checking if kubelet, kubeadm, and kubectl are installed...")
for package in ["kubelet", "kubeadm", "kubectl"]:
    if is_package_installed(package):
        print(f"{package} is installed successfully.")
    else:
        print(f"{package} is not installed.")

