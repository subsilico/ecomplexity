import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode('utf-8').strip()}")
        sys.exit(1)

def create_namespace(namespace):
    print(f"Creating namespace: {namespace}")
    run_command(f"kubectl create namespace {namespace}")

def create_deployment(namespace, deployment_name):
    print(f"Creating deployment: {deployment_name} in namespace: {namespace}")
    deployment_manifest = f"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {deployment_name}
  namespace: {namespace}
spec:
  replicas: 2
  selector:
    matchLabels:
      app: {deployment_name}
  template:
    metadata:
      labels:
        app: {deployment_name}
    spec:
      containers:
      - name: web
        image: nginx
        ports:
        - containerPort: 8000
"""
    run_command(f"echo '{deployment_manifest}' | kubectl apply -f -")

def create_service(namespace, service_name, deployment_name):
    print(f"Creating service: {service_name} in namespace: {namespace}")
    service_manifest = f"""
apiVersion: v1
kind: Service
metadata:
  name: {service_name}
  namespace: {namespace}
spec:
  selector:
    app: {deployment_name}
  ports:
    - protocol: TCP
      port: 8000
  type: ClusterIP
"""
    run_command(f"echo '{service_manifest}' | kubectl apply -f -")

def main():
    namespace = "apptest"
    create_namespace(namespace)
    create_deployment(namespace, "webserver")
    create_service(namespace, "web-service", "webserver")

if __name__ == "__main__":
    main()

