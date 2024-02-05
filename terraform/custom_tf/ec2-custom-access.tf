variable "aws_var" {
  type = map(string)
  default = {
  region_name =  "ap-southeast-1" 
  key_pair_name = "realhrsoft"
  default_vpc_id = "vpc-08bbada9f9013634c"
  default_owner_id = "000348787903"
  default_subnet_id  = "subnet-005fe372ed98fabf0"  
  default_ami = "ami-0fa377108253bf620"

  }
  
}

provider "aws" {
  region = lookup(var.aws_var,"region_name")
  # access_key = ""
  # secret_key = ""
}

# Create a key pair
resource "aws_key_pair" "realhr_key" {
  key_name   = lookup(var.aws_var,"key_pair_name")
  public_key = file("~/.ssh/id_rsa.pub")  # Replace with the path to your public key file
  tags = {
    Name = "realhrsoft"
  }
}

# Create a security group to allow incoming traffic on ports 80, 22, and 443
resource "aws_security_group" "realhrsoft_sg" {
  name        = "realhrsoft_security_group"
  description = "Allow incoming traffic on ports 80, 22, and 443"
  vpc_id      = lookup(var.aws_var,"default_vpc_id")

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
resource "aws_instance" "realhrsoft_instance" {
  ami             = lookup(var.aws_var,"default_ami")  # Replace with the appropriate AMI ID for your region and instance type
  instance_type   = "t2.micro"
  key_name        = aws_key_pair.realhr_key.key_name  #this key name should be same as you created earlyer
  vpc_security_group_ids = [aws_security_group.realhrsoft_sg.id]
 # subnet_id       = aws_subnet.default.id  # Refer to specific instances using count.index
  subnet_id = lookup(var.aws_var,"default_subnet_id")
  # User data for configuring the instance (optional)
  root_block_device {
    delete_on_termination = true
    iops = 3000
    volume_size = 8  # 8 GB in size.
    volume_type = "gp3"
  }
  tags = {
    Name = "Realhrsoft"
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
