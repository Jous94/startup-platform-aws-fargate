output "region" {
  description = "AWS region used for this deployment."
  value       = var.aws_region
}

output "name" {
  description = "Computed base name used for resource naming."
  value       = local.name
}

output "vpc_id" {
  description = "VPC ID."
  value       = aws_vpc.this.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs."
  value       = [for s in aws_subnet.public : s.id]
}

output "alb_dns_name" {
  description = "Public DNS name of the ALB."
  value       = aws_lb.this.dns_name
}

output "alb_security_group_id" {
  description = "Security group ID attached to the ALB."
  value       = aws_security_group.alb.id
}

