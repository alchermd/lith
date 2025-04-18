terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "lith-aws-tf-state-us-east-1"
    key            = "terraform.tfstate"
    dynamodb_table = "terraform-state-lock"
    region         = "us-east-1"
    encrypt        = "true"
  }
}


