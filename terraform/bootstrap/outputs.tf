output "dynamodb_table" {
  value = module.bootstrap.dynamodb_table
}

output "state_bucket" {
  value = module.bootstrap.state_bucket
}

output "ecr_repo_url" {
  value = aws_ecr_repository.repo.repository_url
}

output "ecr_repo_arn" {
  value = aws_ecr_repository.repo.arn
}
