resource "aws_ecr_repository" "repo" {
  name                 = "lith"
  image_tag_mutability = "MUTABLE"
}
