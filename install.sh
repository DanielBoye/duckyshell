#!/bin/bash

# Clone the GitHub repository
git clone https://github.com/DanielBoye/duckyshell.git

# Move into the cloned repository

# Copy the folder to /usr/bin
sudo cp -R duckyshell/ /usr/bin/duckyshell

# Create an alias for running duckyshell.py as 'ducky'
echo "alias ducky='python3 /usr/bin/duckyshell.py'" >> ~/.bashrc

# Reload the bashrc file to apply the alias
source ~/.bashrc

# Provide executable permissions to the program
sudo chmod +x /usr/bin/duckyshell.py

# Cleanup: remove the cloned repository
rm -rf duckyshell

# Installation completed
echo "DuckyShell has been installed. You can now use 'ducky' command to run it."
