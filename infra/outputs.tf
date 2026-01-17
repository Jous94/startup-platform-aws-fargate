output "region" {
  description = "AWS region used for this deployment."
  value       = var.aws_region
}

output "name" {
  description = "Computed base name used for resource naming."
  value       = local.name
}
