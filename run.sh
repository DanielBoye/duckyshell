#!/bin/bash

VERSION=$(python -c "from setup import VERSION; print(VERSION)")
# Function to check and delete folders
check_and_delete_folder() {
    if [ -d "$1" ]; then
        echo "Deleting $1"
        rm -rf "$1"
    fi
}

# Check and delete folders
check_and_delete_folder "duckyshell.egg-info/"
check_and_delete_folder "build/"
check_and_delete_folder "dist/"

# Build the package
python3 setup.py sdist bdist_wheel

# Upload the package to PyPI
twine upload dist/*

# Uninstall previous version
pip uninstall duckyshell

# Install new version
pip install duckyshell

