# duckyshell

A Python-based command-line tool for flashing the USB Rubber Ducky on-the-go!

## Contents

- [Introduction](#introduction)
   - [Key Features](#key-features) 
- [What it is](#what-it-is)
- [How to install](#how-to-install)
- [Motivation](#motivation)
- [Key Features](#key-features)
- [Project Context](#project-context)

## Introduction

Welcome to DuckyShell!

DuckyShell is a powerful and user-friendly Python-based command-line tool designed to simplify the process of programming and flashing your USB Rubber Ducky. Whether you're a penetration tester, ethical hacker, or just curious about the capabilities of the USB Rubber Ducky, DuckyShell provides an efficient and convenient way to work with your Ducky device from the command line.

With DuckyShell, you can set and forget the USB path for connected devices, making it easier to work with your Ducky on the go. The autocomplete tab feature for USB and file commands saves you time and effort, making it a breeze to navigate through directories and filenames.

### Key Features:
- Set and persist the USB path for connected devices, eliminating repetitive configuration tasks.
- Autocomplete tab feature for USB and file commands, enhancing navigation efficiency and reducing errors.
- View connected USB devices to effortlessly identify your Ducky and other storage devices.
- Seamlessly copy inject.bin files to the USB Rubber Ducky for immediate deployment.

DuckyShell comes with an easy-to-use `install.sh` script, ensuring a smooth setup process, and conveniently creating an alias for quick access to the tool.

While working with DuckyShell, please exercise caution and ensure proper permissions to safeguard your system and connected devices.

## What is it

DuckyShell is a command-line tool specifically designed for flashing the USB Rubber Ducky with new payloads while on the move. Whether you need to deploy payloads quickly during a penetration test or experiment with different payloads, DuckyShell simplifies the process and provides an efficient workflow for interacting with your USB Rubber Ducky.

## How to install

1. Open your terminal or command prompt.
2. Download the install.sh script using the following command:

   ```
   curl -o install.sh -LJ https://github.com/DanielBoye/duckyshell/raw/main/install.sh
   ```
4. Provide execute permissions to the script:
   ```
   chmod +x install.sh
   ```
5. Run the installation script:
   ```
   ./install.sh
   ```

## Motivation
DuckyShell was created to address the need for an efficient and intuitive command-line tool for working with the USB Rubber Ducky. The motivation behind its development lies in simplifying the process of flashing inject.bin files onto the USB Rubber Ducky, without compromising on functionality.

## Key Features
- Automated USB Path: DuckyShell saves you time by automatically detecting and setting the USB path for connected devices, eliminating the need for repetitive manual inputs.

- Autocomplete Tab: The autocomplete tab functionality for USB and file commands offers a convenient and error-free method for navigating directories and selecting files.

- Effortless Flashing: With DuckyShell, copying inject.bin files to the USB Rubber Ducky becomes a seamless task, allowing for immediate deployment of payloads.

- USB Device Listing: DuckyShell provides a clear list of currently connected USB devices, simplifying device identification and management.

## Project Context
DuckyShell was developed as part of the final project for CS50, aiming to deliver a practical and efficient solution for programming and deploying payloads on the USB Rubber Ducky. It's user-centric design and robust feature set make it an indispensable tool for USB Rubber Ducky enthusiasts, who want to use the command line.
