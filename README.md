# Startup Platform on AWS (ECS Fargate)

Production-like AWS ECS Fargate platform designed as a startup-grade DevOps portfolio project.

## Goals
- Infrastructure as Code with Terraform
- Containerized API deployed to ECS Fargate
- GitHub Actions CI/CD using AWS OIDC (no long-lived credentials)
- Observability and safe deployment practices

## Current scope (staging)
- VPC, ALB, ECS Fargate service
- ECR for container images
- CloudWatch logs
- Health check endpoint: /health

## Roadmap
- HTTPS with ACM
- RDS PostgreSQL + Secrets Manager
- OpenTelemetry & X-Ray
- Blue/green deployments
