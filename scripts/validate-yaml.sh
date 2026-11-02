#!/usr/bin/env bash
set -euo pipefail

kubectl apply --dry-run=client --validate=false -f k8s/inventory.yaml
