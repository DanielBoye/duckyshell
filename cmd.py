import argparse
import shutil
import os
import cmd

class CopyToUsbCmd(cmd.Cmd):
    intro = 'Welcome to the CopyToUSB command line interface. Type help or ? to list commands.\n'
    prompt = '(CopyToUSB) '

    def do_copy(self, arg):
        """
        Copy a text file to a USB drive.
        Usage: copy [text_file_path] [usb_path]
        """
        parser = argparse.ArgumentParser(description='Copy a text file to a USB drive')
        parser.add_argument('file_path', metavar='file_path', type=str, help='Path to the text file to copy')
        parser.add_argument('usb_path', metavar='usb_path', type=str, help='Path to the mounted USB drive')
        args = parser.parse_args(arg.split())

        # Check if the file exists
        if not os.path.exists(args.file_path):
            print(f"File not found: {args.file_path}")
            return

        # Check if the USB drive is mounted
        if not os.path.exists(args.usb_path):
            print(f"USB drive not found: {args.usb_path}")
            return

        # Check if the file is a text file
        if not args.file_path.lower().endswith('.txt'):
            print(f"Invalid file type: {args.file_path} is not a text file (.txt)")
            return

        # Convert the text file to binary
        binary_file_path = os.path.splitext(args.file_path)[0] + '.bin'
        with open(args.file_path, 'r') as text_file:
            with open(binary_file_path, 'wb') as binary_file:
                binary_file.write(text_file.read().encode('utf-8'))

        # Copy the binary file to the USB drive
        try:
            shutil.copy2(binary_file_path, args.usb_path)
            print(f"File copied to USB drive: {args.usb_path}")
        except Exception as e:
            print(f"Error copying file to USB drive: {e}")

        # Delete the temporary binary file
        os.remove(binary_file_path)

    def do_exit(self, arg):
        """
        Exit the CopyToUSB command line interface.
        """
        print('Exiting CopyToUSB...')
        return True

if __name__ == '__main__':
    CopyToUsbCmd().cmdloop()
