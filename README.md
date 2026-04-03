SecOps Notes

IAM and Access Control
The application uses an IAM role attached to the EC2 instance to access S3. This avoids hardcoding AWS credentials and follows the principle of least privilege.

Secrets Management
No credentials or secrets are stored in the repository. Access is handled through AWS-managed identity instead of static keys.

Network Security
The EC2 instance is configured with a security group that only allows required ports (SSH and HTTP). In a production setup, SSH access would be restricted further.

Container Security
The application runs inside a Docker container to isolate dependencies. In a production environment, this could be improved by using smaller base images and vulnerability scanning.

Monitoring and Logging
Future improvements would include integrating CloudWatch for logging and alerting to monitor system health and detect issues.

Future Improvements
- Use least-privilege IAM policies instead of full S3 access
- Add HTTPS using a load balancer
- Implement CI/CD with security checks