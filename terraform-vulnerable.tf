# VULNERABLE: Terraform configuration with intentionally insecure settings
# DO NOT APPLY TO REAL CLOUD - FOR EDUCATIONAL PURPOSES ONLY

terraform {
  required_version = ">= 0.12"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  # VULNERABLE: No access key restrictions
}

# VULNERABLE: S3 bucket with public read access
resource "aws_s3_bucket" "vuln_lab_bucket" {
  bucket = "vuln-lab-bucket-${random_string.bucket_suffix.result}"
  
  # VULNERABLE: No versioning
  # VULNERABLE: No encryption
  # VULNERABLE: No access logging
}

resource "aws_s3_bucket_public_access_block" "vuln_lab_bucket_pab" {
  bucket = aws_s3_bucket.vuln_lab_bucket.id
  
  # VULNERABLE: Allowing public access
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# VULNERABLE: Public read policy
resource "aws_s3_bucket_policy" "vuln_lab_bucket_policy" {
  bucket = aws_s3_bucket.vuln_lab_bucket.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.vuln_lab_bucket.arn}/*"
      }
    ]
  })
}

# VULNERABLE: EC2 instance with overly permissive security group
resource "aws_instance" "vuln_lab_instance" {
  ami           = "ami-0c02fb55956c7d316"  # VULNERABLE: Old AMI
  instance_type = "t2.micro"
  
  # VULNERABLE: No IAM role restrictions
  # VULNERABLE: No user data security
  
  vpc_security_group_ids = [aws_security_group.vuln_lab_sg.id]
  
  # VULNERABLE: No encryption at rest
  # VULNERABLE: No backup policies
  
  tags = {
    Name = "vuln-lab-instance"
    Environment = "lab"
  }
}

# VULNERABLE: Security group allowing all traffic
resource "aws_security_group" "vuln_lab_sg" {
  name_prefix = "vuln-lab-sg-"
  description = "VULNERABLE: Overly permissive security group"
  
  # VULNERABLE: Allowing all ingress traffic
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "udp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  # VULNERABLE: Allowing all egress traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "vuln-lab-security-group"
  }
}

# VULNERABLE: IAM role with overly permissive policies
resource "aws_iam_role" "vuln_lab_role" {
  name = "vuln-lab-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}

# VULNERABLE: IAM policy with full access
resource "aws_iam_policy" "vuln_lab_policy" {
  name        = "vuln-lab-policy"
  description = "VULNERABLE: Overly permissive IAM policy"
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "*"
        Resource = "*"
      }
    ]
  })
}

# VULNERABLE: Attaching overly permissive policy to role
resource "aws_iam_role_policy_attachment" "vuln_lab_policy_attachment" {
  role       = aws_iam_role.vuln_lab_role.name
  policy_arn = aws_iam_policy.vuln_lab_policy.arn
}

# VULNERABLE: Instance profile with overly permissive role
resource "aws_iam_instance_profile" "vuln_lab_profile" {
  name = "vuln-lab-profile"
  role = aws_iam_role.vuln_lab_role.name
}

# VULNERABLE: RDS instance with weak security
resource "aws_db_instance" "vuln_lab_db" {
  identifier = "vuln-lab-db"
  
  engine         = "postgres"
  engine_version = "12.0"  # VULNERABLE: Old version
  instance_class = "db.t2.micro"
  
  allocated_storage     = 20
  max_allocated_storage = 100
  storage_type          = "gp2"
  
  db_name  = "vuln_lab"
  username = "admin"
  password = "FAKE_password123"  # VULNERABLE: Weak password
  
  # VULNERABLE: Publicly accessible
  publicly_accessible = true
  
  # VULNERABLE: No encryption
  storage_encrypted = false
  
  # VULNERABLE: No backup retention
  backup_retention_period = 0
  
  # VULNERABLE: No monitoring
  monitoring_interval = 0
  
  # VULNERABLE: No security group restrictions
  vpc_security_group_ids = [aws_security_group.vuln_lab_sg.id]
  
  tags = {
    Name = "vuln-lab-database"
  }
}

# VULNERABLE: Lambda function with overly permissive execution role
resource "aws_lambda_function" "vuln_lab_lambda" {
  filename         = "lambda_function.zip"
  function_name    = "vuln-lab-lambda"
  role            = aws_iam_role.vuln_lab_lambda_role.arn
  handler         = "index.handler"
  runtime         = "python3.8"
  
  # VULNERABLE: No environment variable encryption
  environment {
    variables = {
      DATABASE_URL = "postgresql://admin:FAKE_password123@vuln-lab-db:5432/vuln_lab"
      API_KEY      = "FAKE_1234567890abcdef"
      SECRET_TOKEN = "FAKE_vulnerable_token_for_lab_only"
    }
  }
}

# VULNERABLE: Lambda execution role with full access
resource "aws_iam_role" "vuln_lab_lambda_role" {
  name = "vuln-lab-lambda-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# VULNERABLE: Lambda execution policy with full access
resource "aws_iam_role_policy" "vuln_lab_lambda_policy" {
  name = "vuln-lab-lambda-policy"
  role = aws_iam_role.vuln_lab_lambda_role.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "*"
        Resource = "*"
      }
    ]
  })
}

# Random string for bucket naming
resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
  upper   = false
}

# VULNERABLE: CloudTrail logging disabled
resource "aws_cloudtrail" "vuln_lab_trail" {
  name                          = "vuln-lab-trail"
  s3_bucket_name               = aws_s3_bucket.vuln_lab_bucket.id
  include_global_service_events = false  # VULNERABLE: Not logging global service events
  is_multi_region_trail        = false   # VULNERABLE: Single region only
  enable_logging               = false  # VULNERABLE: Logging disabled
  enable_log_file_validation   = false  # VULNERABLE: No log file validation
  
  event_selector {
    read_write_type                 = "All"
    include_management_events       = false  # VULNERABLE: Not logging management events
    data_resource {
      type   = "AWS::S3::Object"
      values = ["${aws_s3_bucket.vuln_lab_bucket.arn}/*"]
    }
  }
}

# VULNERABLE: GuardDuty disabled
resource "aws_guardduty_detector" "vuln_lab_detector" {
  enable = false  # VULNERABLE: Threat detection disabled
}

# VULNERABLE: Config rules disabled
resource "aws_config_configuration_recorder" "vuln_lab_recorder" {
  name     = "vuln-lab-recorder"
  role_arn = aws_iam_role.vuln_lab_role.arn
  
  recording_group {
    all_supported                 = false  # VULNERABLE: Not recording all resource types
    include_global_resource_types = false  # VULNERABLE: Not including global resources
  }
}

# VULNERABLE: KMS key with weak encryption
resource "aws_kms_key" "vuln_lab_key" {
  description             = "VULNERABLE: Weak KMS key"
  deletion_window_in_days = 7  # VULNERABLE: Short deletion window
  
  # VULNERABLE: No key rotation
  enable_key_rotation = false
  
  # VULNERABLE: Weak key policy
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "*"  # VULNERABLE: Allows all principals
        }
        Action   = "kms:*"
        Resource = "*"
      }
    ]
  })
}

# VULNERABLE: Secrets Manager with weak configuration
resource "aws_secretsmanager_secret" "vuln_lab_secret" {
  name                    = "vuln-lab-secret"
  description             = "VULNERABLE: Weak secrets configuration"
  recovery_window_in_days = 0  # VULNERABLE: Immediate deletion
  
  # VULNERABLE: No rotation
  rotation_lambda_arn = null
  
  tags = {
    Name = "vuln-lab-secret"
  }
}

# VULNERABLE: WAF disabled
resource "aws_wafv2_web_acl" "vuln_lab_waf" {
  name  = "vuln-lab-waf"
  scope = "REGIONAL"
  
  # VULNERABLE: No rules defined
  default_action {
    allow {}
  }
  
  # VULNERABLE: No logging
  visibility_config {
    cloudwatch_metrics_enabled = false
    metric_name                = "vuln-lab-waf"
    sampled_requests_enabled  = false
  }
}

# VULNERABLE: VPC Flow Logs disabled
resource "aws_flow_log" "vuln_lab_flow_log" {
  iam_role_arn    = aws_iam_role.vuln_lab_role.arn
  log_destination = aws_s3_bucket.vuln_lab_bucket.arn
  traffic_type    = "ALL"
  
  # VULNERABLE: Flow logs disabled
  log_destination_type = "s3"
  log_format = ""  # VULNERABLE: No custom log format
}

# VULNERABLE: Output exposing sensitive information
output "database_password" {
  value = aws_db_instance.vuln_lab_db.password
  description = "VULNERABLE: Exposing database password in output"
}

output "api_key" {
  value = "FAKE_1234567890abcdef"
  description = "VULNERABLE: Exposing API key in output"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.vuln_lab_bucket.bucket
  description = "VULNERABLE: Exposing S3 bucket name"
}

output "kms_key_id" {
  value = aws_kms_key.vuln_lab_key.key_id
  description = "VULNERABLE: Exposing KMS key ID"
}

output "secrets_manager_arn" {
  value = aws_secretsmanager_secret.vuln_lab_secret.arn
  description = "VULNERABLE: Exposing Secrets Manager ARN"
}
