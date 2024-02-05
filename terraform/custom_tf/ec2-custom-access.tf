provider "aws" {
  region = "ap-southeast-1"
  access_key = "AKIAQAFGKCS74Y433EM7"
  secret_key = "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"
}

# Create a key pair
resource "aws_key_pair" "singapoor_key" {
  key_name   = "singapoor_key"
  public_key = file("~/.ssh/id_rsa.pub")  # Replace with the path to your public key file
  tags = {
    Name = "sg_key"
  }
}

# Create a security group to allow incoming traffic on ports 80, 22, and 443
resource "aws_security_group" "test_sg" {
  name        = "test_security_g"
  description = "Allow incoming traffic on ports 80, 22, and 443"
  vpc_id      = "vpc-08bbada9f9013634c"
  #owner_id = "000348787903"

#Outbound traffic rule for all traffic to your instance 
  egress {
    from_port = 0
    to_port =  0
    protocol = "-1" #all protocol
    cidr_blocks = ["0.0.0.0/0"]
  }
# inbound traffic rule for your instance
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
resource "aws_instance" "test_instance_sg" {
  #count = length(var.availability_zones)
  ami             = "ami-0fa377108253bf620"  # Replace with the appropriate AMI ID for your region and instance type
  instance_type   = "t2.micro"
  key_name        = aws_key_pair.singapoor_key.key_name  #this key name should be same as you created earlyer
  vpc_security_group_ids = [aws_security_group.test_sg.id]
 # subnet_id       = aws_subnet.default.id  # Refer to specific instances using count.index
  subnet_id       = "subnet-005fe372ed98fabf0"  # Refer to specific instances using count.index

  #subnet_id       = aws_subnet.default.id  # Replace with your desired subnet ID within the default VPC

  # User data for configuring the instance (optional)

  root_block_device {
    volume_size = 8  # 60GB EBS volume
  }
  tags = {
    Name = "Test instance singapor"
  }
}

# Use the default AWS VPC
# resource "aws_vpc" "default" {
#   cidr_block = "172.31.0.0/16"
#   enable_dns_support = true
#   enable_dns_hostnames = true
#   instance_tenancy = "default"
  
# }

# Use the default AWS subnet within the default VPC
# variable "availability_zones" {
#   default = ["ap-southeast-1a","ap-southeast-1b","ap-southeast-1c"]
  
# }
#resource "aws_subnet" "default" {
  #count = length(var.availability_zones)
 # vpc_id      = "vpc-08bbada9f9013634c"
  # cidr_block              = "172.31.0.0/16"
  # availability_zone        = "ap-southeast-1a"  # Replace with your desired availability zone
  # map_public_ip_on_launch  = true
#}
