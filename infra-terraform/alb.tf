data "aws_lb_target_group" "backend_tg" {
  name = "backend-tg"
}

data "aws_lb" "app_lb" {
  name = "${var.project_name}-alb"
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = data.aws_lb.app_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = data.aws_lb_target_group.backend_tg.arn
  }
}

