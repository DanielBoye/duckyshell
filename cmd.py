import cmd
import os


class DuckyShell(cmd.Cmd):
    intro = "Hak5 USB Rubber Ducky CLI\nType 'help' to list available commands."
    prompt = "(DuckyShell) "
    usb_path = None

    def do_copy_to_usb(self, file_path):
        """Copy a payload from a text file to the USB Rubber Ducky"""
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

    def do_set_usb_path(self, usb_path):
        """Set the USB path for future commands"""
        self.usb_path = usb_path
        print(f"USB path set to: {usb_path}")

    def do_quit(self, arg):
        """Exit the DuckyShell"""
        print("Exiting DuckyShell...")
        return True


if __name__ == '__main__':
    shell = DuckyShell()
    shell.cmdloop()
