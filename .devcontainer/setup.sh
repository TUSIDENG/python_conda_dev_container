#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_NAME="python_conda_env"
REQUIREMENTS_FILE="$WORKSPACE_ROOT/requirements.txt"

# in devconainer.json,已经设置了
# echo "Configure git safe directory..."
# git config --global --add safe.directory "${WORKSPACE_ROOT}"

echo "Initialize Conda..."
if [ -f "/opt/conda/etc/profile.d/conda.sh" ]; then
  source "/opt/conda/etc/profile.d/conda.sh"
else
  echo "ERROR: Conda initialization script not found."
  exit 1
fi

echo "Ensure Conda environment '${ENV_NAME}' exists..."
if ! conda env list | awk '{print $1}' | grep -qx "${ENV_NAME}"; then
  conda create -n "${ENV_NAME}" python=3.11 -y
else
  echo "Conda environment '${ENV_NAME}' already exists."
fi

echo "Activate Conda environment '${ENV_NAME}'..."
conda activate "${ENV_NAME}"

echo "Install packages from requirements.txt..."
if [ -f "${REQUIREMENTS_FILE}" ] && [ -s "${REQUIREMENTS_FILE}" ]; then
  pip install -r "${REQUIREMENTS_FILE}"
else
  echo "No packages to install: '${REQUIREMENTS_FILE}' is missing or empty."
fi