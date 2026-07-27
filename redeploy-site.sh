#!/bin/bash

set -e

# Wrapped in a function so bash reads the whole body into memory before
# executing — otherwise `git reset --hard` rewrites this file mid-run
# and bash picks up mixed old/new content for the remaining lines.
main() {
    cd /root/MLH-portfolio
    git fetch && git reset origin/main --hard

    docker compose -f docker-compose.prod.yml down
    docker compose -f docker-compose.prod.yml up -d --build
}

main "$@"
