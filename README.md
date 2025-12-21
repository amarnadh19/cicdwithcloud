## Aim of this project is:

to build a CI/CD pipeline using github actions that deploys a sample JAVA or Python application.

Destination deployment is on EKS or GKE.  Current EKS.

.
├── .github/
│   ├── workflows/                # CORE: GitHub Action definitions
│   │   ├── ci.yml                # Continuous Integration (Build & Test)
│   │   └── deploy.yml            # Continuous Deployment (Push to Prod/Staging)
│   └── ACTIONS_README.md         # Documentation specific to workflows
│
├── docker/                       # Containerization specifics
│   ├── Dockerfile                # Defines how to package the python
│
├── infra/                        # Infrastructure as Code (Target Environment)
│   ├── k8s/                      # Kubernetes manifests (Deployment, Service, Ingress)
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── terraform/                # Terraform scripts (if provisioning Cloud resources)
│   │   ├── main.tf
│   │   └── variables.tf
│   └── helm/                     # (Alternative) Helm charts if using Helm
│
├── scripts/                      # Helper scripts executed by the Workflow
│   ├── health-check.sh           # Script to verify app is up after deploy
│   └── env-setup.sh              # Script to set dynamic environment variables
│
├── .gitignore                    # standard git ignore file
└── README.md                     # Project documentation


Step 1: Create a github action job to build the docker image 

Step 2: Create DEV Environment and added secrets for AWS credentials 

Step 3: To push to ECR repository


