#!/bin/bash

# Update package list and install Python and pip
echo "Updating package list..."
sudo apt update

echo "Installing Python and pip..."
sudo apt install -y python3 python3-pip

# Install python virtual environment
echo "Setting up virtual environment..."
sudo apt install python3-venv

# Install Pillow for image processing
echo "Installing Pillow..."
pip3 install pillow

echo "All dependencies installed successfully!"
