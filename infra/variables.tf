variable "aws_region" {
  description = "AWS region to deploy resources into."
  type        = string
  default     = "eu-central-1"
}

variable "project" {
  description = "Project name used for resource naming."
  type        = string
  default     = "startup-platform"
}

variable "env" {
  description = "Environment name (e.g., staging, prod)."
  type        = string
  default     = "staging"
}

variable "app_port" {
  description = "Application container port."
  type        = number
  default     = 8080
}

variable "github_org" {
  description = "GitHub organization or username (used for OIDC trust policy)."
  type        = string
  default     = "Jous94"
}

variable "github_repo" {
  description = "GitHub repository name (used for OIDC trust policy)."
  type        = string
  default     = "startup-platform-aws-fargate"
}

locals {
  # A single place to control naming across AWS resources.
  name = "${var.project}-${var.env}"

  tags = {
    Project = var.project
    Env     = var.env
  }
}
