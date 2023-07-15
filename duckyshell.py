#!/usr/bin/env python3

import cmd
import subprocess
import os
import yaml

# Config file path
CONFIG_FILE_PATH = "config.yaml"

# Class for the CLI program
class DuckyShell(cmd.Cmd):
    
    # Clears the screen 
    os.system(f"clear")
    
    # Prints out the intro
    intro = "\nHak5 USB Rubber Ducky CLI\n\nType 'help' to list available commands.\n"
    
    # Prompt for the CLI
    prompt = "ducky_sh3ll > "
    
    # Setting the usb path to None for now
    usb_path = None
    file_path = None

    def __init__(self):
        super().__init__()
        self.load_usb_path()

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
            
    def complete_set_file(self, text, line, begidx, endidx):
        """
        Called to perform tab-completion on the file path argument of set_file command.
        """
        # Get a list of files and directories in the current directory
        current_dir = os.getcwd()
        files_and_dirs = os.listdir(current_dir)

        # Filter the list based on the current text being entered
        options = [entry for entry in files_and_dirs if entry.startswith(text)]

        return options

    # Function for copying the file to the usb
    def do_run(self, arg):
        # Copy the payload from the binary file to the USB Rubber Ducky
        if not self.usb_path:
            print("USB path not provided. Use 'set_usb_path' command to set it.")
            return

        if not self.file_path:
            print("File path not provided. Use 'set_file_path' command to set it.")
            return

        # Check if the file is a binary file
        if not self.file_path.endswith('.bin'):
            print(f"Invalid file type: {self.file_path} is not a text file (.txt)")
            return


        # Copy the binary file to the USB drive
        os.system(f"cp {self.file_path} {self.usb_path}")
        print(f"File copied to USB drive: {self.usb_path}")

        # Delete the temporary text file
        os.remove(self.file_path)

    # Setting the usb path for more future commands
    def do_set_usb(self, usb_path):
        # Set the USB path for future commands
        self.usb_path = usb_path
        self.save_usb_path()
        print(f"USB path set to: {usb_path}")

    def do_set_file(self, line):
        """
        Set the file path for future copy operations.
        Usage: set_file <file_path>
        """
        file_path = line.strip()

        # Check if the file path exists
        if not os.path.exists(file_path):
            print("File path does not exist.")
            return

        # Set the file path for future copy operations
        self.file_path = file_path
        print(f"File path set to: {file_path}")

    # Listing the connected USB devices
    def do_list_usb(self, arg):
        """
        List the connected USB devices.

        Usage: list_usb

        List the currently connected USB devices.
        """
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


    # List the config directory
    def do_config(self, arg):
        # List the directory where the config file is stored
        config_dir = os.path.dirname(CONFIG_FILE_PATH)
        print(f"Config file directory: {config_dir}")

    def emptyline(self):
        pass
    
    # Exit command 1
    def do_quit(self, arg):
        # Exit the DuckyShell
        print("Exiting DuckyShell...")
        return True

    # Exit command 2
    def do_exit(self, arg):
        # Exit the DuckyShell
        print("Exiting DuckyShell...")
        return True


# Function for running the program
if __name__ == '__main__':
    shell = DuckyShell()
    shell.cmdloop()
