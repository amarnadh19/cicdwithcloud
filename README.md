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
│   ├── Dockerfile                # Defines how to package the Java JAR
│   └── docker-compose.yml        # (Optional) For local testing
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
├── pom.xml                       # (or build.gradle) Required at root for the runner to build
├── .gitignore                    # standard git ignore file
└── README.md                     # Project documentation



