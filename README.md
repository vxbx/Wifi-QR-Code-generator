# Wifi-QR-Code-generator
If you have many people needing to connect to your wifi, this will be a potential quality of life upgrade,
I got inspired while using a online variant. 
This is completly offline and the only output is the png-file created.

This is a QR-Code-generator for creating QR-code for automatically connecting to WIFI-network using camera on your device. This has popup for inpu of SSID, network key and encryption type. Outputs to PNG.

This is completly offline and the only output is the png-file created.

Popup for input of SSID, key and encr. type.
Popup for the output location and the filename of the PNG-file. 
Default QR-Code PNG-name includes the SSID and current date and time.

To run this you need to have python installed, and the library qrcode.
If you wany to make it executable you can use the command pyinstaller.

If you are using Anaconda, you can use these commands in the Anaconda Prompt: 

#this adds library 
conda install -c conda-forge qrcode

#this installs pyinstaller
conda install -c anaconda pyinstaller

#this compiles exe
pyinstaller --onefile wifi_qrcode_generator.py
