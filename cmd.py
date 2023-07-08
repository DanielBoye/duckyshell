import cmd
import os
import yaml

# Config file path
CONFIG_FILE_PATH = "/usr/bin/duckyshell_config.yaml"

# Class for the CLI program
class DuckyShell(cmd.Cmd):
    
    # Prints out the intro
    intro = "Hak5 USB Rubber Ducky CLI\nType 'help' to list available commands."
    
    # Promt for the CLI
    prompt = "ducky_sh3ll > "
    
    # Setting the usb path to None for now
    usb_path = None

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

    # Function for copying the file to the usb
    def do_copy_to_usb(self, file_path):
        # Copy a payload from a text file to the USB Rubber Ducky
        if not self.usb_path:
            print("USB path not provided. Use 'set_usb_path' command to set it.")
            return

        # Check if the file is a text file
        if not file_path.endswith('.txt'):
            print(f"Invalid file type: {file_path} is not a text file (.txt)")
            return

        # Convert the text file to binary
        binary_file_path = file_path[:-3] + 'bin'
        with open(file_path, 'r') as text_file, open(binary_file_path, 'wb') as binary_file:
            for line in text_file:
                binary_file.write(line.encode('utf-8'))

        # Copy the binary file to the USB drive
        os.system(f"cp {binary_file_path} {self.usb_path}")
        print(f"File copied to USB drive: {self.usb_path}")

        # Delete the temporary binary file
        os.remove(binary_file_path)

    # Setting the usb path for more future commands
    def do_set_usb_path(self, usb_path):
        # Set the USB path for future commands
        self.usb_path = usb_path
        self.save_usb_path()
        print(f"USB path set to: {usb_path}")

    # Listing the connected USB device 
    def do_list_usb(self, arg):
        # List the currently connected USB devices
        if self.usb_path:
            usb_list = os.listdir(self.usb_path)
            if usb_list:
                print("Connected USB devices:")
                for device in usb_list:
                    print(device)
            else:
                print("No USB devices found in the specified path.")
        else:
            print("USB path not provided. Use 'set_usb_path' command to set it.")

    # List the config directory
    def do_list_config_dir(self, arg):
        # List the directory where the config file is stored
        config_dir = os.path.dirname(CONFIG_FILE_PATH)
        print(f"Config file directory: {config_dir}")

    # Exit command 1
    def do_quit(self, arg):
        """Exit the DuckyShell"""
        print("Exiting DuckyShell...")
        return True

    # Exit command 2
    def do_exit(self, arg):
        """Exit the DuckyShell"""
        print("Exiting DuckyShell...")
        return True


# Function for running the program
if __name__ == '__main__':
    shell = DuckyShell()
    shell.cmdloop()
