import subprocess

def run_docker_container(image_name):
    try:
        subprocess.run(["docker", "run", "-it", image_name, "R"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    image_name = "my-app:latest"  # Replace with your Docker image name

    print('Remember to type: library("plumber")')
    print("""IF: Error in library("plumber") : there is no package called ‘plumber’""")
    print("""THEN: instll.packages("plumber")""")

    run_docker_container(image_name)


