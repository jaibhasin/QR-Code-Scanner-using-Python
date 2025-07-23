# QR Code Scanner Using Python

This project is a simple QR code scanner that opens a webcam, displays the feed, and prints the data from any QR code detected in the frame. It is implemented in Python using OpenCV and pyzbar.

## Requirements
- Python 3.12 or compatible
- `opencv-python`
- `pyzbar`
- The [ZBar](https://github.com/mchehab/zbar) shared library (`libzbar0` on Debian/Ubuntu)

## Setup
1. Install Python dependencies:
   ```bash
   pip install opencv-python pyzbar
   ```
2. Install the system package providing the ZBar shared library. On Debian/Ubuntu based systems:
   ```bash
   sudo apt-get update
   sudo apt-get install libzbar0
   ```

## Usage
Run the script with Python:
```bash
python main.py
```
Press `q` to exit the scanner.

## Known Issues
If the ZBar shared library is not installed, running the script will produce the following error:
```
ImportError: Unable to find zbar shared library
```
Install `libzbar0` or the equivalent package for your platform to resolve this.
