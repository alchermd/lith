#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR=$(pwd)
TF_ROOT_DIR="${ROOT_DIR}/terraform"
BOOTSTRAP_DIR="${TF_ROOT_DIR}/bootstrap"

for d in $TF_ROOT_DIR $BOOTSTRAP_DIR; do
  cd "$d"
  terraform destroy -auto-approve
done
