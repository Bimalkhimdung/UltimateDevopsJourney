provider "aws" {
  region = "us-east-1"  # Set your desired region
}

# Create a key pair
resource "aws_key_pair" "test_key" {
  key_name   = "test_key"
  public_key = file("~/.ssh/id_rsa.pub")  # Replace with the path to your public key file
}

# Create a security group to allow incoming traffic on ports 80, 22, and 443
resource "aws_security_group" "test_sg" {
  name        = "test_security_group"
  description = "Allow incoming traffic on ports 80, 22, and 443"
  vpc_id      = aws_vpc.default.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a T4g.small EC2 instance
resource "aws_instance" "test_instance" {
  ami             = "ami-05d47d29a4c2d19e1"  # Replace with the appropriate AMI ID for your region and instance type
  instance_type   = "t4g.small"
  key_name        = aws_key_pair.test_key.key_name
  vpc_security_group_ids = [aws_security_group.test_sg.id]
  subnet_id       = aws_subnet.default.id  # Replace with your desired subnet ID within the default VPC

  # User data for configuring the instance (optional)

  root_block_device {
    volume_size = 8  # 60GB EBS volume
  }
  tags = {
    Name = "Test instance"
  }
}

# Use the default AWS VPC
resource "aws_vpc" "default" {
  cidr_block = "172.31.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
}

# Use the default AWS subnet within the default VPC
resource "aws_subnet" "default" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = "172.31.32.0/20"
  availability_zone        = "us-east-1a"  # Replace with your desired availability zone
  map_public_ip_on_launch  = true
}
