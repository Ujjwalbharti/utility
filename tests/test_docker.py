import os
import pytest
import subprocess

@pytest.fixture(scope='module')
def docker_image():
    """Retrieve the Docker image name from environment variables."""
    image_name = os.getenv('IMAGE_NAME', 'utility-test:linux-amd64')
    
    # Check if the image exists before yielding it
    result = subprocess.run(['docker', 'images', '-q', image_name], check=True, capture_output=True)
    assert result.stdout.strip() != b'', f"The Docker image '{image_name}' does not exist."

    yield image_name

def test_docker_image_exists(docker_image):
    """Test if the Docker image exists."""
    result = subprocess.run(['docker', 'images', '-q', docker_image], check=True, capture_output=True)
    assert result.stdout.strip() != b'', f"The Docker image '{docker_image}' does not exist."

def test_installed_packages(docker_image):
    """Test if specific packages are installed in the Docker image."""
    packages = ['curl', 'mysql', 'psql', 'redis-cli', 'wget']
    
    for package in packages:
        result = subprocess.run(
            ['docker', 'run', '--rm', docker_image, 'sh', '-c', f'command -v {package}'],
            check=True, capture_output=True
        )
        assert result.stdout.strip() != b'', f"{package} is not installed in the Docker image '{docker_image}'."

if __name__ == '__main__':
    pytest.main()
