import subprocess
import importlib.util
import sys

def install_and_import(package):
    try:
        importlib.util.find_spec(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

def check_service_configuration(service_name, namespace='default'):
    kubernetes.config.load_kube_config()  # Load config from ~/.kube/config
    v1 = kubernetes.client.CoreV1Api()
    
    try:
        service = v1.read_namespaced_service(service_name, namespace)
        print(f"Service {service_name} Configuration:")
        print(f"Type: {service.spec.type}")
        print(f"Ports: {service.spec.ports}")
        print(f"Selector: {service.spec.selector}")
    except kubernetes.client.exceptions.ApiException as e:
        print(f"An error occurred: {e}")

def setup_port_forwarding(service_name, namespace='default', port=8000):
    try:
        subprocess.run(["kubectl", "port-forward", f"svc/{service_name}", f"{port}:{port}", "-n", namespace])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during port forwarding: {e}")

if __name__ == '__main__':
    install_and_import('kubernetes')
    service_name = 'myapp-service'  # Replace with your service name
    check_service_configuration(service_name)
    #setup_port_forwarding(service_name, port=8000)

