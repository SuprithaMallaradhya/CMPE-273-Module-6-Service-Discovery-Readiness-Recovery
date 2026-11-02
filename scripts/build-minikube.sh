#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

if ! minikube image build -t cmpe273-inventory:1.0 "$PROJECT_DIR"; then
  echo "Image build failed; Kubernetes resources were not applied." >&2
  exit 1
fi
kubectl apply -f k8s/inventory.yaml
kubectl rollout status deployment/inventory --timeout=120s
kubectl rollout status deployment/inventory-client --timeout=120s
