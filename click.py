import os
import click

# Will not be using this script, maybe some click functionalities
@click.group()
@click.option('--usb-path', type=click.Path(), help='Path to the USB drive')
@click.pass_context
def ducky_cli(ctx, usb_path):
    """Hak5 USB Rubber Ducky CLI"""
    ctx.ensure_object(dict)
    ctx.obj['usb_path'] = usb_path


@ducky_cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.pass_context
def copy_to_usb(ctx, file_path):
    # Copy a payload from a text file to the USB Rubber Ducky
    usb_path = ctx.obj.get('usb_path')
    if not usb_path:
        click.echo("USB path not provided. Use '--usb-path' option or set it using 'set-usb-path' command.")
        return

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


@ducky_cli.command()
@click.argument('usb_path', type=click.Path())
@click.pass_context
def set_usb_path(ctx, usb_path):
    """Set the USB path for future commands"""
    ctx.obj['usb_path'] = usb_path
    click.echo(f"USB path set to: {usb_path}")


if __name__ == '__main__':
    ducky_cli(obj={})
