# DevOps Assessment Assignment

## 📌 Overview
This project demonstrates a complete **DevOps workflow** for a backend system using **FastAPI, Celery, Redis**, containerization, **Infrastructure as Code (Terraform)**, and **CI/CD with GitHub Actions**, deployed on **AWS using managed services**.

The solution focuses on:
- Containerization best practices
- Infrastructure provisioning using Terraform
- CI/CD automation
- Cloud-native deployment using AWS ECS Fargate
- Managed Redis using Amazon ElastiCache
- Observability using CloudWatch Logs

---

## 🏗️ Architecture Overview

**High-level flow:**

Browser / Client
|
v
Application Load Balancer (ALB)
|
v
ECS Fargate (FastAPI Backend)
|
v
Amazon ElastiCache (Redis)
|
v
ECS Fargate (Celery Worker)


**AWS Services Used**
- Amazon ECS (Fargate)
- Application Load Balancer (ALB)
- Amazon ElastiCache (Redis)
- Amazon ECR
- AWS CloudWatch Logs
- AWS IAM
- Terraform (IaC)
- GitHub Actions (CI/CD)

---

## 📂 Repository Structure

devops-assignment/
│
├── backend/                         # Backend application
│   ├── main.py                      # FastAPI app (API endpoints)
│   ├── worker.py                    # Celery worker
│   ├── Dockerfile                   # Backend Docker image
│   ├── Dockerfile.worker            # Worker Docker image
│   └── __init__.py
│
├── frontend/                        # Simple UI
│   └── index.html                   # Triggers API & polls task status
│
├── infra-terraform/                 # Infrastructure as Code (Terraform)
│   ├── main.tf                      # Provider & common config
│   ├── variables.tf                 # Input variables
│   ├── ecr.tf                       # ECR repositories
│   ├── ecs.tf                       # ECS cluster & security group
│   ├── task.tf                      # ECS task definitions
│   ├── ecs_service.tf               # ECS services (Fargate)
│   ├── alb.tf                       # Application Load Balancer
│   ├── redis.tf                     # ElastiCache (Redis)
│   └── outputs.tf                   # ALB & ECR outputs
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml                # CI/CD pipeline (GitHub Actions)
│
├── docker-compose.yml               # Local container setup
├── requirements.txt                 # Python dependencies
├── instructions.md                  # Developer setup guide
├── journey.md                       # Design & implementation journey
└── README.md                        # Project documentation

---

## ⚙️ Application Components

### Backend – FastAPI
- `POST /notify/` → Enqueues a Celery task
- `GET /task_status/{task_id}` → Returns task status
- `GET /health` → Health check endpoint

### Worker – Celery
- Consumes tasks from Redis
- Processes background jobs asynchronously

### Redis
- Used as Celery broker and result backend
- Managed via Amazon ElastiCache in cloud

### Frontend
- Simple HTML page
- Triggers background task and polls for status

---

## 🐳 Run Locally (Docker Compose)

### Prerequisites
- Docker
- Docker Compose

### Commands
```bash
docker compose build
docker compose up
