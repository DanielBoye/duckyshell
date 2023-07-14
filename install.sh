#!/bin/bash

echo -e "Installer script for duckyshell\n\n"

# Clone the GitHub repository
echo -e "Cloning the Github repository\n"
git clone https://github.com/DanielBoye/duckyshell.git

# Copy the folder to /usr/bin
echo -e "Copying folders\n"
sudo cp -R duckyshell/ /usr/bin/duckyshell

# Create an alias for running duckyshell.py as 'ducky'
echo -e "Creating aliases\n"
echo "alias ducky='python3 /usr/bin/duckyshell/duckyshell.py'" >> ~/.bashrc

# Reload the bashrc file to apply the alias
echo -e "Reload the .bashrc file\n"
source ~/.bashrc

# Provide executable permissions to the program
echo -e "Make the program executable\n"
sudo chmod +x /usr/bin/duckyshell/duckyshell.py

# Cleanup: remove the cloned repository
echo -e "Clean up install\n" 
rm -rf duckyshell/

# Installation completed
echo -e "DuckyShell has been installed.\n"
echo -e "You can now use 'ducky' command to run it.\n"
