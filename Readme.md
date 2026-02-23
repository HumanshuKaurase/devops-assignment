
# DevOps Assessment Assignment

## 📌 Overview
This project demonstrates a complete **DevOps workflow** for a backend system using **FastAPI, Celery, Redis**, containerization, **Infrastructure as Code (Terraform)**, and **CI/CD with GitHub Actions**, deployed on **AWS managed services**.

The solution focuses on:
- Containerization best practices
- Infrastructure provisioning using Terraform
- CI/CD automation
- Cloud-native deployment using AWS ECS Fargate
- Managed Redis using Amazon ElastiCache
- Observability using CloudWatch Logs

---

## 🏗️ Architecture Overview

### High-level flow

```

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

```

### AWS Services Used
- Amazon ECS (Fargate)
- Application Load Balancer (ALB)
- Amazon ElastiCache (Redis)
- Amazon ECR
- AWS CloudWatch Logs
- AWS IAM
- Terraform (IaC)
- GitHub Actions (CI/CD)

## 📂 Repository Structure



devops-assignment/
├── backend/
│   ├── main.py
│   ├── worker.py
│   ├── Dockerfile
│   ├── Dockerfile.worker
│   └── **init**.py
│
├── frontend/
│   └── index.html
│
├── infra-terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── ecr.tf
│   ├── ecs.tf
│   ├── task.tf
│   ├── ecs_service.tf
│   ├── alb.tf
│   ├── redis.tf
│   └── outputs.tf
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── docker-compose.yml
├── requirements.txt
├── instructions.md
├── journey.md
└── README.md



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
- Managed using Amazon ElastiCache in AWS

### Frontend
- Simple HTML UI
- Triggers background task and polls status

---

## 🐳 Run Locally (Docker Compose)

### Prerequisites
- Docker
- Docker Compose

### Commands
```bash
docker compose build
docker compose up
````

```


