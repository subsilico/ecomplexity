import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8').strip()}"

def check_kubernetes_cluster():
    print("Checking Kubernetes cluster status...")
    cluster_info = run_command("kubectl cluster-info")
    print(cluster_info + "\n")

def check_kubectl_configuration():
    print("Checking kubectl configuration...")
    config = run_command("kubectl config view")
    print(config + "\n")

def check_cluster_nodes():
    print("Listing Kubernetes cluster nodes...")
    nodes = run_command("kubectl get nodes")
    print(nodes + "\n")

def check_current_context():
    print("Checking current kubectl context...")
    current_context = run_command("kubectl config current-context")
    print(current_context + "\n")

def list_all_contexts():
    print("Listing all kubectl contexts...")
    contexts = run_command("kubectl config get-contexts")
    print(contexts + "\n")

def main():
    check_kubernetes_cluster()
    check_kubectl_configuration()
    check_cluster_nodes()
    check_current_context()
    list_all_contexts()

if __name__ == "__main__":
    main()

