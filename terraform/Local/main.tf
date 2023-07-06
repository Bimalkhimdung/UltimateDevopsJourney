terraform {
# service provider section
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
#This aws version  section
  required_version = ">= 1.2.0"
}
 #this is  region section
provider "aws" {
  region  = "us-west-2"
}
# Main resources defining sections 
resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  #Name of instanc
  tags = {
    Name = "Terraform_Demo"
  }
}


