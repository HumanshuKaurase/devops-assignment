data "aws_ecr_repository" "backend" {
  name = "${var.project_name}-backend"
}

data "aws_ecr_repository" "worker" {
  name = "${var.project_name}-worker"
}
