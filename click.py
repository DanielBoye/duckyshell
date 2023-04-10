import os
import click

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('usb_path', type=click.Path())
def copy_to_usb(file_path, usb_path):
    # Check if the file is a text file
    if not file_path.endswith('.txt'):
        click.echo(f"Invalid file type: {file_path} is not a text file (.txt)")
        return

    # Convert the text file to binary
    binary_file_path = file_path[:-3] + 'bin'
    with open(file_path, 'r') as text_file, open(binary_file_path, 'wb') as binary_file:
        for line in text_file:
            binary_file.write(line.encode('utf-8'))

    # Copy the binary file to the USB drive
    os.system(f"cp {binary_file_path} {usb_path}")
    click.echo(f"File copied to USB drive: {usb_path}")

    # Delete the temporary binary file
    os.remove(binary_file_path)

if __name__ == '__main__':
    copy_to_usb()
