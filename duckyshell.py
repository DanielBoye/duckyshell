#!/usr/bin/env python3

import cmd
import subprocess
import os
import yaml
import glob
import re

# Config file path
CONFIG_FILE_PATH = "config.yaml"

# Class for the CLI program
class DuckyShell(cmd.Cmd):
    
    # Clears the screen 
    os.system(f"clear")
    
    # Prints out the intro
    intro = "\nHak5 USB Rubber Ducky CLI\n\nType 'help' to list available commands or 'help <command>' to get help for a specific command.\n"    
    # Prompt for the CLI
    prompt = "ducky_sh3ll > "
    
    # Setting the usb path to None for now
    usb_path = None
    file_path = None

    def __init__(self):
        super().__init__()
        self.load_usb_path()
    
    # Help messages for each command
    help_messages = {
        'usb': 'Set the USB path for connected USB devices.',
        'file': 'Set the file to the designated inject.bin you want.',
        'list': 'List the connected USB devices.',
        'run': 'Copy the inject.bin to the USB Rubber Ducky.',
        'quit': 'Exit the DuckyShell.',
        'exit': 'Exit the DuckyShell.',
    }

    # Function for setting the usb path
    def load_usb_path(self):
        # Load the USB path from the config file
        if os.path.exists(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH, 'r') as config_file:
                config = yaml.safe_load(config_file)
                self.usb_path = config.get('usb_path')

    # Function for saving the usb path
    def save_usb_path(self):
        # Save the USB path to the config file
        config = {'usb_path': self.usb_path}
        with open(CONFIG_FILE_PATH, 'w') as config_file:
            yaml.safe_dump(config, config_file)
    
    # Tab autocomplete for file function
    def complete_file(self, text, line, begidx, endidx):
        # Get a list of files and directories in the current directory
        current_dir = os.getcwd()
        files_and_dirs = os.listdir(current_dir)

        # Filter the list based on the current text being entered
        options = [entry for entry in files_and_dirs if entry.startswith(text)]

        return options
    
    # Tab autocomplete for usb function
    def complete_usb(self, text, line, begidx, endidx):
        # Get a list of files and directories in the current directory
        current_dir = os.getcwd()
        files_and_dirs = os.listdir(current_dir)

        # Filter the list based on the current text being entered
        options = [entry for entry in files_and_dirs if entry.startswith(text)]

        # Returning results
        return options
    
    # Function to only select connected usb devices
    def get_connected_usb_devices(self):
        devices = glob.glob('/dev/sd*[!0-9]')
        return [os.path.basename(device) for device in devices]

    # Function for copying the file to the usb
    def do_run(self, arg):
        # Check for USB path provided
        if not self.usb_path:
            print("USB path not provided. Use 'set_usb_path' command to set it.")
            return
        # Check for file path provided
        if not self.file_path:
            print("File path not provided. Use 'set_file_path' command to set it.")
            return

        # Check if the file is a binary file
        if not self.file_path.endswith('.bin'):
            print(f"Invalid file type: {self.file_path} is not a text file (.txt)")
            return

        # Copy the binary file to the USB Rubber Ducky
        os.system(f"cp {self.file_path} {self.usb_path}")
        print(f"File copied to USB drive: {self.usb_path}")

        # Delete the temporary text file
        os.remove(self.file_path)

   # Set the USB path for connected USB devices
    def do_usb(self, line):
        usb_path = line.strip()
        # Check if the USB device is connected
        usb_devices = [device[0] for device in self.get_connected_usb_devices()]
        if usb_path not in usb_devices:
            print("USB device is not connected.")
            return    
        # Set the USB path for future commands
        self.usb_path = usb_path
        self.save_usb_path()
        print(f"USB path set to: {usb_path}")

    # Set file to the designated file you want
    def do_file(self, line):
        file_path = line.strip()

        # Check if the file path exists
        if not os.path.exists(file_path):
            print("File path does not exist.")
            return

        # Check if the file path has the correct extension
        if not re.match(r"inject.bin", file_path):
            print("Invalid file format. Only 'inject.bin' files are allowed.")
            return

        # Set the file path for future copy operations
        self.file_path = file_path
        print(f"File path set to: {file_path}")

    # Listing the connected USB devices
    def do_list(self, arg):
        output = subprocess.check_output(['lsblk', '-o', 'NAME,MODEL', '-n', '-l']).decode('utf-8').strip()
        lines = output.split('\n')
        devices = [line.split() for line in lines]
        usb_devices = [device for device in devices if device and (device[0].startswith('sd') or device[0].startswith('hd'))]
        if usb_devices:
            print("Connected USB devices:")
            for device in usb_devices:
                if len(device) >= 2:
                    print(f"Name: {device[0]}   Model: {device[1]}")
                else:
                    print(f"Name: {device[0]}   Model: Unknown")
        else:
            print("No USB devices found.")

    def emptyline(self):
        pass
    
    def do_help(self, arg):
        """
        List available commands with their usage.
        Usage: help [command]
        """
        if arg:
            # Show help for a specific command
            if arg in self.help_messages:
                print(self.help_messages[arg])
            else:
                print(f"Command '{arg}' not found.")
        else:
            # Show help for all commands
            print("\nAvailable commands:")
            for command, help_message in self.help_messages.items():
                print(f"{command}: {help_message}")
            print("\n")
    
    # Exit command 1
    def do_quit(self, arg):
        # Exit the DuckyShell
        print("Exiting DuckyShell...")
        return True

    # Exit command 2
    def do_exit(self, arg):
        # Exit the DuckyShell
        print("\nExiting DuckyShell...\n")
        return True


# Function for running the program
if __name__ == '__main__':
    shell = DuckyShell()
    shell.cmdloop()
