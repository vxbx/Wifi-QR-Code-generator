# Wifi-QR-Code-generator

Do you have a popular WIFI? This will be a potential quality of life upgrade. 
I got inspired while using an online variant. 
This is completely offline, and the only output is the PNG file created.

This is a QR code generator for creating QR codes to automatically connect to a Wi-Fi network using the camera on your device. It has pop-ups for input of SSID, network key, and encryption type, and outputs to PNG.

This is a completely offline operation after the installation is done, and the only output is the PNG file created.
Nothing is done in the "cloud", everything is done locally.

Pop-up for input of SSID, key, and encryption type.
Pop-up for the output location and filename of the PNG file.
Default QR code PNG name: "wifi_qrcode_{ssid}_{current_datetime}.png".

To run this, you need to have Python installed, and the library qrcode.
If you want to make it executable, you can use the command pyinstaller.

If you are using Anaconda, you can use these commands in the Anaconda Prompt:
# This adds the library:
conda install -c conda-forge qrcode
# This installs pyinstaller:
conda install -c anaconda pyinstaller
# This is optional, but needed if you want an exe file. Compiles the exe file:
pyinstaller --onefile wifi_qrcode_generator.py
