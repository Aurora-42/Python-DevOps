# Python-DevOps
A template for Python projects with DevOps tools, including development environment, testing, image building and deployment.

## Getting Started

### Docker Development
1. **Dependencies**
    * [Install Docker](https://docs.docker.com/get-docker/)
    * [Install Docker Compose](https://docs.docker.com/compose/install/)
2. **Environment Setup**
    * Build the Docker image: `./scripts/build.sh`
    * Run the Docker container: `./scripts/dev.sh`

### Local Development
1. **Dependencies**
    * [Install Python](https://www.python.org/downloads/)
    * [Install Python Virtual Environment](https://virtualenv.pypa.io/en/latest/installation.html)
2. **Environment Setup**
    * Create a virtual environment: `python3 -m venv .venv`
    * Activate the virtual environment: `source .venv/bin/activate`
    * Install dependencies: `pip install -r requirements.txt`

You can now run the project with `python3 -m src`

To run the tests, run `pytest`
