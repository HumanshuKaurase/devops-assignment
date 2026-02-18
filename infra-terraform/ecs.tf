resource "aws_ecs_cluster" "this" {
  name = "${var.project_name}-cluster"
}

data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

data "aws_security_group" "ecs_sg" {
  filter {
    name   = "group-name"
    values = ["${var.project_name}-sg"]
  }
}
