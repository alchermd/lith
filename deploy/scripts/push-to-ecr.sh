#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR=$(pwd)
SRC_DIR="${ROOT_DIR}/src"
TF_ROOT_DIR="${ROOT_DIR}/terraform"
BOOTSTRAP_DIR="${TF_ROOT_DIR}/bootstrap"

cd "$BOOTSTRAP_DIR"
ECR_REPO_URL=$(jq -r .ecr_repo_url.value < tf-output.json)
ECR_URL=$(echo "$ECR_REPO_URL" | cut -d "/" -f 1)
ECR_REPO_NAME=$(echo "$ECR_REPO_URL" | cut -d "/" -f 2)
ECR_REPO_IMAGE_TAG="latest"

cd "$SRC_DIR"
aws ecr get-login-password | docker login --username AWS --password-stdin "$ECR_URL"

docker build -t "$ECR_REPO_NAME:$ECR_REPO_IMAGE_TAG" -t "$ECR_REPO_URL:$ECR_REPO_IMAGE_TAG" .
docker push "$ECR_REPO_URL:$ECR_REPO_IMAGE_TAG"
