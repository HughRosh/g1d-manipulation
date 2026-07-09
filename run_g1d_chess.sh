#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

MOVE="${1:-e2e4}"
ARM="${2:-right}"

python -m g1d_chess.main --move "$MOVE" --arm "$ARM"
