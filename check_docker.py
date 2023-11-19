import os
import re

def is_valid_dockerfile(dockerfile_path):
    # Check if the Dockerfile exists
    if not os.path.isfile(dockerfile_path):
        return False, "Dockerfile not found."

    # Read the Dockerfile content
    with open(dockerfile_path, 'r') as f:
        dockerfile_content = f.read()

    # Check if the Dockerfile contains a valid FROM instruction
    from_match = re.search(r'^\s*FROM\s+(.+)', dockerfile_content, re.MULTILINE)
    if not from_match:
        return False, "Dockerfile does not contain a valid FROM instruction."

    # Check if WORKDIR is set
    if 'WORKDIR' not in dockerfile_content:
        return False, "Dockerfile does not set the WORKDIR."

    # Check if COPY or ADD instructions are used to copy files into the container
    if 'COPY' not in dockerfile_content and 'ADD' not in dockerfile_content:
        return False, "Dockerfile does not use COPY or ADD instructions to copy files into the container."

    return True, "Dockerfile is valid."

if __name__ == "__main__":
    dockerfile_path = "Dockerfile"  # Update with the path to your Dockerfile
    is_valid, message = is_valid_dockerfile(dockerfile_path)
    if is_valid:
        print("Dockerfile is sane and valid.")
    else:
        print("Dockerfile inspection result:", message)
