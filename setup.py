"""Setup configuration for Docker Compose Manager."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
else:
    requirements = []

setup(
    name="docker-compose-manager",
    version="1.0.0",
    author="Enterprise Team",
    author_email="team@example.com",
    description="Enterprise-level system for managing multitenant Docker Compose v3 deployments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nullroute-commits/docker_compose_pr",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "scripts"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dcm-init=init:main",
            "dcm-manage=manage:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
