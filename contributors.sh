#!/usr/bin/env bash
# This script prints the list of contributors to the repository.
# Usage: ./contributors.sh
git log --pretty=format:"%an" | sort | uniq -c | sort -rn
