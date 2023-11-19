import subprocess
import sys

def run_command(command, capture_output=True):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        return result.stdout.decode('utf-8').strip() if capture_output else ""
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode('utf-8').strip()}")
        sys.exit(1)

def check_kubelet_logs():
    print("1. Checking kubelet logs...")
    logs = run_command("journalctl -u kubelet -n 50")
    print(logs if logs else "No recent kubelet logs found.\n")

def check_kubeadm_config():
    print("2. Checking Kubernetes configuration files in /etc/kubernetes/...")
    config_files = run_command("ls /etc/kubernetes/")
    print(config_files if config_files else "No Kubernetes configuration files found in /etc/kubernetes/.\n")

    print("2.1 Checking Kubernetes manifest files in /etc/kubernetes/manifests/...")
    manifests = run_command("ls /etc/kubernetes/manifests/")
    if manifests:
        print("Manifest files found:")
        for manifest in manifests.split('\n'):
            print(f" - {manifest}")
            print("   Content:")
            content = run_command(f"cat /etc/kubernetes/manifests/{manifest}")
            print(content + "\n")
    else:
        print("No manifest files found in /etc/kubernetes/manifests/.\n")


def check_cluster_info():
    print("3. Checking Kubernetes cluster info...")
    cluster_info = run_command("kubectl cluster-info", capture_output=False)
    print(cluster_info if cluster_info else "Unable to retrieve cluster info.\n")

# Rest of the functions remain the same

def main():
    check_kubelet_logs()
    check_kubeadm_config()
    check_cluster_info()
    # Remaining checks

if __name__ == "__main__":
    main()
