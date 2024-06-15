# Getting Started

## Prerequisites

- Python 3.11
- Poetry -> pip install poetry
- Docker (optional, for containerized deployment) [Container have been tested in Window environment, for Mac might be needed some adjustment]
- Make (to use Makefile commands)

## Running Application on local machine
    
1. Install dependencies:

   ```sh
   make install_env
   ```
   
2. Run Backend Application:
    
   ```sh
   make run_backend
   ```
   
3. Run Frontend Application:

   ```sh
   make run_backend
   ```
   
## Running Application on docker containers

1. Build images
   
   ```sh
   make docker_build_app
   ```
   
2. Run containers

   ```sh
   make docker_app_up
   ```
   
   Note: In the logs, it may appear that the app is deployed on 0.0.0.0:<port>, but it is actually accessible on localhost:<port>.



