🚀 Cloud DevOps Project on Google Cloud

📌 Project Overview - 
This project demonstrates an end-to-end DevOps pipeline on Google Cloud, covering application development, containerization, CI/CD automation, deployment, and monitoring.
A Flask-based application is containerized using Docker, built and deployed through GitHub Actions, hosted on Google Compute Engine, and monitored using Prometheus and Grafana.

🏗️ Architecture - 
Developer → GitHub → GitHub Actions → Docker Build
→ Artifact Registry → Compute Engine VM → Monitoring Stack
(Prometheus → Grafana)

🛠️ Tech Stack - 
Python (Flask)
Docker
GitHub Actions
Google Cloud (Compute Engine, Artifact Registry)
Prometheus
Grafana

⚙️ Setup Instructions - 
Clone Repository
git clone https://github.com/prava-dev-hash/gcp-cloud-devops-project.git
cd gcp-cloud-devops-project

Build Docker Image - 
docker build -t cloud-devops-app .

Run Application - 
docker run -d -p 5000:5000 cloud-devops-app
Access Application
http://<VM-IP>:5000

🔄 CI/CD Pipeline - 
The project uses GitHub Actions to automate the workflow.
On every push to the main branch, the pipeline builds the Docker image and pushes it to Google Artifact Registry.
This ensures faster and consistent deployments.

📦 Container Registry - 
Docker images are stored in Google Artifact Registry.
us-central1-docker.pkg.dev/<project-id>/cloud-devops-repo/cloud-devops-app

📊 Monitoring & Observability - 
Prometheus is used to collect application and system metrics.
Grafana is used to visualize these metrics through dashboards.

Example query used in Grafana:
up - 
A value of 1 indicates the service is running, while 0 indicates failure.

📸 Screenshots - 
Application running in browser:
<img width="624" height="300" alt="image" src="https://github.com/user-attachments/assets/7c253f5e-d73d-4104-a7e8-1479aefbc77b" />

Prometheus dashboard:
<img width="624" height="317" alt="image" src="https://github.com/user-attachments/assets/4bb110ad-dcad-40c1-a1de-1d84b250c044" />

Grafana dashboard:
<img width="624" height="314" alt="image" src="https://github.com/user-attachments/assets/573c576d-6665-40f3-b416-0e042f3b9541" />


🚀 Key Highlights - 
End-to-end DevOps pipeline implementation
Containerized application deployment
Cloud-based hosting on Google Cloud
Integrated monitoring and visualization
Scalable architecture with future enhancements

🔮 Future Enhancements - 
Kubernetes deployment using GKE
Load balancing and auto scaling
HTTPS and domain integration
Prometheus alerting configuration
Infrastructure as Code using Terraform

👩‍💻 Author - 
Pravallika P
https://github.com/prava-dev-hash

⭐ Conclusion - 
This project demonstrates practical DevOps implementation using modern tools and cloud services. It highlights real-world skills in CI/CD, containerization, cloud deployment, and monitoring.
