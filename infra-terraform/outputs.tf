output "alb_url" {
  value = data.aws_lb.app_lb.dns_name
}

output "backend_ecr_url" {
  value = data.aws_ecr_repository.backend.repository_url
}

output "worker_ecr_url" {
  value = data.aws_ecr_repository.worker.repository_url
}
