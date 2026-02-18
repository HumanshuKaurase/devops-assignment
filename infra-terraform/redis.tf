data "aws_elasticache_subnet_group" "redis" {
  name = "redis-subnet"
}

data "aws_elasticache_cluster" "redis" {
  cluster_id = "${var.project_name}-redis"
}

