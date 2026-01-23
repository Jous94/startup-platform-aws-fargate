resource "aws_security_group" "db" {
  name        = "${local.name}-db-sg"
  description = "DB security group"
  vpc_id      = aws_vpc.this.id

  ingress {
    description     = "Postgres from API"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.api.id]
  }

  egress {
    description = "All egress"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(local.tags, { Name = "${local.name}-db-sg" })
}

resource "aws_db_subnet_group" "this" {
  name       = "${local.name}-db-subnets"
  subnet_ids = [for s in aws_subnet.public : s.id]

  tags = merge(local.tags, { Name = "${local.name}-db-subnets" })
}

resource "aws_db_instance" "postgres" {
  identifier        = "${local.name}-db"
  engine            = "postgres"
  instance_class    = "db.t4g.micro"
  allocated_storage = 20

  db_name  = local.db_secret.DB_NAME
  username = local.db_secret.DB_USER
  password = local.db_secret.DB_PASSWORD

  publicly_accessible = false
  skip_final_snapshot = true
  deletion_protection = false

  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.this.name

  tags = merge(local.tags, { Name = "${local.name}-db" })
}

output "db_endpoint" {
  value = aws_db_instance.postgres.address
}
