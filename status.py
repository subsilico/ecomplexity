import subprocess
import sys

def run_command(command, capture_output=False):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout if capture_output else f"Command {' '.join(command)} executed successfully."
    except subprocess.CalledProcessError as e:
        print(f"Error executing {' '.join(command)}: {e.stderr}")
        sys.exit(1)

def check_pod_logs(pod_name):
    print(f"Checking logs for pod: {pod_name}")
    return run_command(["kubectl", "logs", pod_name], capture_output=True)

def get_pod_names(app_name, namespace="default"):
    pod_list = run_command(["kubectl", "get", "pods", "-l", f"app={app_name}", "-n", namespace, "-o", "jsonpath={.items[*].metadata.name}"], capture_output=True)
    return pod_list.split()

def check_pods_logs(app_name, namespace="default"):
    pod_names = get_pod_names(app_name, namespace)
    for pod_name in pod_names:
        print(check_pod_logs(pod_name))

def check_pods_status(deployment_name, namespace="default"):
    print(f"Checking status of pods for '{deployment_name}'...")
    print(run_command(["kubectl", "get", "pods", "-l", f"app={deployment_name}", "-n", namespace, "-o", "wide"], capture_output=True))

def check_pods_status2(deployment_name, namespace="default"):
    print(f"Checking status of pods for '{deployment_name}'...")

    # Get the list of pod names
    pod_list = run_command(["kubectl", "get", "pods", "-l", f"app={deployment_name}", "-n", namespace, "-o", "jsonpath={.items[*].metadata.name}"], capture_output=True)
    pods = pod_list.split()

    # Describe each pod
    for pod in pods:
        print(f"Describing pod: {pod}")
        description = run_command(["kubectl", "describe", "pod", pod, "-n", namespace], capture_output=True)
        print(description)


def main():
    deployment_file = 'deployment.yaml'  # Change this to your deployment.yaml file path
    service_file = 'service.yaml'        # Change this to your service.yaml file path
    app_name = 'myapp'                   # Change this to your app's name

    check_pods_status(app_name)
    check_pods_status2(app_name)
    check_pods_logs(app_name)

if __name__ == "__main__":
    main()

