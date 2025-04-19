output "ec2_instance_public_ip" {
  value = aws_instance.web_server.public_ip
}
