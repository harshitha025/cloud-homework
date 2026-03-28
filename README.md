# Cloud Engineering Homework – AWS Deployment

## Overview

This project demonstrates a simple but complete cloud deployment workflow on AWS. I built a FastAPI application, containerized it using Docker, and deployed it on an EC2 instance. The application is exposed publicly and integrates with Amazon S3 for basic storage operations.

The focus here was not just getting something running, but doing it in a way that reflects how services are typically deployed and accessed in a real environment.

---

## Architecture

The request flow is straightforward:

* A user sends an HTTP request through the browser
* The request reaches an EC2 instance running a Docker container
* Inside the container, a FastAPI application handles the request
* When hitting the `/upload` endpoint, the app generates a file and uploads it to S3
* Access to S3 is handled through an IAM role attached to the EC2 instance

This keeps the application stateless and avoids embedding credentials directly in the code.

---

## AWS Services Used

* **EC2** – Used as the compute layer to host the application
* **Docker** – Ensures consistent runtime between local and cloud environments
* **S3** – Used for simple object storage
* **IAM** – Provides secure, temporary access to AWS resources

---

## Running the Application Locally

1. Navigate to the `app` directory

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Start the server:

   ```
   uvicorn main:app --reload
   ```

4. Access the app at:

   ```
   http://127.0.0.1:8000
   ```

---

## Deployment Approach

The deployment was done manually to keep control over each step:

* Launched an Ubuntu-based EC2 instance
* Configured security groups to allow SSH (22) and HTTP (80)
* Installed Docker and Git on the instance
* Pulled the project from GitHub
* Built the Docker image directly on EC2
* Ran the container and exposed it on port 80

This setup keeps things simple while still reflecting a realistic deployment flow. The deployment was intentionally done manually instead of using managed services to better understand the underlying infrastructure and control each step of the process.

---

## S3 Integration

The application includes an `/upload` endpoint that creates a file and uploads it to an S3 bucket using `boto3`.

Instead of using access keys, the EC2 instance is assigned an IAM role with S3 permissions. The AWS SDK automatically picks up these temporary credentials, which avoids hardcoding secrets and aligns with standard AWS practices. The application relies on AWS SDK’s default credential provider chain, which automatically retrieves temporary credentials from the IAM role.

---

## Security Considerations

* IAM roles are used instead of static credentials
* Only required ports (22 for SSH and 80 for HTTP) are exposed
* No secrets are stored in the repository
* The application runs inside a container, isolating dependencies from the host

---

## Limitations and Improvements

This setup is intentionally simple, but in a production scenario I would:

* Move the deployment to ECS or Kubernetes for better scalability
* Add a CI/CD pipeline (e.g., GitHub Actions) for automated builds and deployments
* Introduce monitoring and logging using CloudWatch
* Add HTTPS using an Application Load Balancer
* Improve API validation and error handling

---

## Final Thoughts

The goal of this project was to demonstrate a clear understanding of how application code moves from local development to a running service in the cloud. The setup uses basic AWS building blocks, but focuses on correct usage—especially around containerization and secure access to resources.

## Challenges Faced

During development, I ran into a few issues that required debugging:

* Docker build initially failed due to Windows-specific dependencies (pywin32) being included in requirements.txt. This was resolved by minimizing dependencies to only required packages.
* There was a mismatch between local (Windows) and container (Linux) environments, which highlighted the importance of cross-platform compatibility.
* SSH and key management required reconfiguration after losing the initial key pair.

These issues helped reinforce how environment differences and dependency management impact deployments.
