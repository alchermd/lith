#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR=$(pwd)
TF_ROOT_DIR="${ROOT_DIR}/terraform"
BOOTSTRAP_DIR="${TF_ROOT_DIR}/bootstrap"

cd "$BOOTSTRAP_DIR"
terraform init
terraform apply -auto-approve
