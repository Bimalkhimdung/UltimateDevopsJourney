### syntax
<Block type> <"Block name"> "<Block lable>" {
#block body 
<Identifier> = <Expression>

}
eg: 
resource "aws_vpc" "main"{

    cidr_block = var.base_cidr_block
}