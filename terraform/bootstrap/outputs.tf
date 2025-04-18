output "dynamodb_table" {
  value = module.bootstrap.dynamodb_table
}

output "state_bucket" {
  value = module.bootstrap.state_bucket
}
