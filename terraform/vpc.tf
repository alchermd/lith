data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "main" {
  cidr_block = "10.16.0.0/16"
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table" "route_table" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}

resource "aws_subnet" "reserved_a" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.0.0/20"
  availability_zone = data.aws_availability_zones.available.names[0]
}

resource "aws_subnet" "db_a" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.16.0/20"
  availability_zone = data.aws_availability_zones.available.names[0]
}

resource "aws_subnet" "app_a" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.32.0/20"
  availability_zone = data.aws_availability_zones.available.names[0]
}

resource "aws_subnet" "web_a" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.16.48.0/20"
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true
}

resource "aws_route_table_association" "web_a_rt_assoc" {
  route_table_id = aws_route_table.route_table.id
  subnet_id      = aws_subnet.web_a.id
}

resource "aws_subnet" "reserved_b" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.64.0/20"
  availability_zone = data.aws_availability_zones.available.names[1]
}

resource "aws_subnet" "db_b" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.80.0/20"
  availability_zone = data.aws_availability_zones.available.names[1]
}

resource "aws_subnet" "app_b" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.96.0/20"
  availability_zone = data.aws_availability_zones.available.names[1]
}

resource "aws_subnet" "web_b" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.112.0/20"
  availability_zone = data.aws_availability_zones.available.names[1]
}

resource "aws_route_table_association" "web_b_rt_assoc" {
  route_table_id = aws_route_table.route_table.id
  subnet_id      = aws_subnet.web_b.id
}

resource "aws_subnet" "reserved_c" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.128.0/20"
  availability_zone = data.aws_availability_zones.available.names[2]
}

resource "aws_subnet" "db_c" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.144.0/20"
  availability_zone = data.aws_availability_zones.available.names[2]
}

resource "aws_subnet" "app_c" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.160.0/20"
  availability_zone = data.aws_availability_zones.available.names[2]
}

resource "aws_subnet" "web_c" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.16.176.0/20"
  availability_zone = data.aws_availability_zones.available.names[2]
}

resource "aws_route_table_association" "web_c_rt_assoc" {
  route_table_id = aws_route_table.route_table.id
  subnet_id      = aws_subnet.web_c.id
}
