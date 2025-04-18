module "bootstrap" {
  source = "trussworks/bootstrap/aws"

  region        = local.region
  account_alias = local.account_alias
}
