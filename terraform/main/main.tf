

variable "aws_client" {
    type = map(string)
    default = {
    region = "ap-southeast-1"
    vpc = "vpc-08bbada9f9013634c"
    ami = "ami-0fa377108253bf620"
    instance_type = "t2.micro"
    subnet = "subnet-005fe372ed98fabf0"
    public_ip = true
  
    keyname = "singapoor_key"
    secgroupname = "test_security_g1"

    }
  
}
provider "aws" {
  region = lookup(var.aws_client, "region")
  # access_key = ""
  # secret_key = ""
}

resource "aws_security_group" "sg_test" {
  name = lookup(var.aws_client, "secgroupname")
  description = lookup(var.aws_client, "secgroupname")
  vpc_id = lookup(var.aws_client, "vpc")

  // To Allow SSH Transport
  ingress {
    from_port = 22
    protocol = "tcp"
    to_port = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  // To Allow Port 80 Transport
  ingress {
    from_port = 80
    protocol = "tcp"
    to_port = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }

  lifecycle {
    create_before_destroy = true
  }
}


resource "aws_instance" "project-iac" {
  ami = lookup(var.aws_client, "ami")
  instance_type = lookup(var.aws_client, "instance_type")
  subnet_id = lookup(var.aws_client, "subnet") #FFXsubnet2
  associate_public_ip_address = lookup(var.aws_client, "public_ip")
  key_name = lookup(var.aws_client, "keyname")


  vpc_security_group_ids = [
    aws_security_group.sg_test.id
  ]
  root_block_device {
    delete_on_termination = true
    iops = 150
    volume_size = 8
    volume_type = "gp3"
  }
  tags = {
    Name ="bimal"
    Environment = "DEV"
    OS = "UBUNTU"
    Managed = "IAC"
  }

  depends_on = [ aws_security_group.sg_test ]
}


output "ec2instance" {
  value = aws_instance.project-iac.public_ip
}