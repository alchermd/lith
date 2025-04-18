#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR=$(pwd)
TF_ROOT_DIR="${ROOT_DIR}/terraform"

cd "$TF_ROOT_DIR"
terraform fmt -check
