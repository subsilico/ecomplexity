import subprocess
import sys

def run_command(command, capture_output=False):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout if capture_output else f"Command {' '.join(command)} executed successfully."
    except subprocess.CalledProcessError as e:
        print(f"Error executing {' '.join(command)}: {e.stderr}")
        sys.exit(1)

def apply_kubernetes_config(deployment_file, service_file):
    print("Applying Kubernetes deployment...")
    print(run_command(["kubectl", "apply", "-f", deployment_file]))

    print("Applying Kubernetes service...")
    print(run_command(["kubectl", "apply", "-f", service_file]))

def check_deployment_status(deployment_name, namespace="default"):
    print(f"Checking status of deployment '{deployment_name}'...")
    print(run_command(["kubectl", "get", "deployment", deployment_name+"-deployment", "-n", namespace, "-o", "wide"], capture_output=True))

def check_pods_status(deployment_name, namespace="default"):
    print(f"Checking status of pods for '{deployment_name}'...")
    print(run_command(["kubectl", "get", "pods", "-l", f"app={deployment_name}", "-n", namespace, "-o", "wide"], capture_output=True))

def check_service_status(service_name, namespace="default"):
    print(f"Checking status of service '{service_name}'...")
    print(run_command(["kubectl", "get", "service", service_name+"-service", "-n", namespace, "-o", "wide"], capture_output=True))

def main():
    deployment_file = 'deployment.yaml'  # Change this to your deployment.yaml file path
    service_file = 'service.yaml'        # Change this to your service.yaml file path
    app_name = 'myapp'        # Change this to your app's name

    apply_kubernetes_config(deployment_file, service_file)
    check_deployment_status(app_name)
    check_pods_status(app_name)
    check_service_status(app_name)

if __name__ == "__main__":
    main()

