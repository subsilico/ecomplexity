import subprocess
import sys

def run_command(command, check=True, capture_output=False, ignore_errors=False):
    try:
        result = subprocess.run(command, check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip() if capture_output else ""
    except subprocess.CalledProcessError as e:
        if ignore_errors:
            return e.stderr.decode('utf-8').strip()
        else:
            print(f"An error occurred: {e}")
            sys.exit(1)

def check_process(process):
    result = run_command(["pgrep", "-f", process], capture_output=True, ignore_errors=True)
    return bool(result)

def start_service(service):
    print(f"Attempting to start {service}...")
    run_command(["sudo", "systemctl", "start", service], ignore_errors=True)

def check_kubernetes_status():
    print("Checking kubeadm cluster status...")
    cluster_status = run_command(["kubeadm", "config", "view"], capture_output=True, ignore_errors=True)
    if "apiVersion" in cluster_status:
        print("Kubernetes cluster configuration found.")
    else:
        print("Kubernetes cluster configuration not found or not accessible.")

def main():
    print("Checking if kubelet is running...")
    if check_process("kubelet"):
        print("kubelet is running.")
    else:
        print("kubelet is not running.")
        start_service("kubelet")
        if check_process("kubelet"):
            print("kubelet started successfully.")
        else:
            print("Failed to start kubelet. Please check manually.")

    check_kubernetes_status()

if __name__ == "__main__":
    main()

