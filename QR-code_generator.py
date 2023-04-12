import qrcode
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime

def generate_qrcode():
    ssid = ssid_entry.get()
    password = password_entry.get()
    auth_type = auth_type_var.get()

    if ssid == "":
        print("Error: SSID cannot be empty")
        return

    qr_data = f"WIFI:S:{ssid};T:{auth_type};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Generate filename with current date, time, and SSID
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"wifi_qrcode_{ssid}_{current_datetime}.png"
    
    # Open file dialog to select storage location
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")],
                                             initialfile=filename)
    if file_path:
        img.save(file_path)
        print(f"Success: QR code saved as {file_path}")
    else:
        print("Error: No file path selected")

# Create a Tkinter window
root = tk.Tk()
root.title("WiFi QR Code Generator")

# Create input labels and entries
ssid_label = tk.Label(root, text="SSID:")
ssid_label.pack()
ssid_entry = tk.Entry(root)
ssid_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

auth_type_label = tk.Label(root, text="Authentication Type:")
auth_type_label.pack()
auth_type_var = tk.StringVar(value="WPA")
auth_type_radio1 = tk.Radiobutton(root, text="WPA", variable=auth_type_var, value="WPA")
auth_type_radio2 = tk.Radiobutton(root, text="WEP", variable=auth_type_var, value="WEP")
auth_type_radio1.pack()
auth_type_radio2.pack()

# Create generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode)
generate_button.pack()

root.mainloop()
