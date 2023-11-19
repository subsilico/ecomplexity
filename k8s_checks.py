import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def check_kubernetes_setup():
    #print("Checking Kubernetes Cluster Status...")
    #print(run_command("kubectl cluster-info"))

    print("Checking the Nodes...")
    print(run_command("kubectl get nodes"))

    print("Running a Simple Test Deployment...")
    print(run_command("kubectl create deployment nginx --image=nginx"))

    print("Checking Deployments...")
    print(run_command("kubectl get deployments"))

    print("Checking the Pod Status...")
    print(run_command("kubectl get pods"))

    print("Exposing the Deployment...")
    print(run_command("kubectl expose deployment nginx --type=LoadBalancer --port=80"))

    print("Checking Services...")
    print(run_command("kubectl get services"))

    print("Describing Nodes...")
    print(run_command("kubectl describe nodes"))

def main():
    check_kubernetes_setup()

if __name__ == "__main__":
    main()

