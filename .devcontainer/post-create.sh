#!/bin/sh
# Runs once in the workspace folder after the container is created.
# Add project setup that needs the mounted workspace here, such as installing
# dependencies. Keep each step safe to run again.
set -eu

# Git refuses to use a repository owned by a different user, which happens
# when the host user's ID differs from the container user's. Trust the
# mounted workspace.
if ! git config --global --get-all safe.directory | grep -qxF "$PWD"; then
    git config --global --add safe.directory "$PWD"
fi
