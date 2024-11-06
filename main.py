import os
import customtkinter as ctk
import qrcode
import tkinter.messagebox as msgbox  # Import the tkinter messagebox

# Create the main window
root = ctk.CTk()

# Functions
def generate():
    name = entry1.get()
    text = entry2.get()

    # Create the Qr_codes directory if it does not exist
    if not os.path.exists("Qr_codes"):
        os.makedirs("Qr_codes")

    # Generate the QR code
    qr = qrcode.make(text)

    # Save the QR code as an image
    qr.save(f"Qr_codes/{name}.png")

    # Show a success popup message
    msgbox.showinfo("Success", f"QR Code '{name}' generated and saved successfully!")


# Set window title
root.title("Qreate by Tled")

# Label for QR Name
label1 = ctk.CTkLabel(root, text="Enter QR Name :", font=("Arial", 16))
label1.pack(pady=1)

# Entry widget for QR Name
entry1 = ctk.CTkEntry(root, placeholder_text="Enter your QR name...", width=200, font=("Arial", 14))
entry1.pack(pady=0)

# Label for URL
label2 = ctk.CTkLabel(root, text="Enter URL :", font=("Arial", 16))
label2.pack(pady=1)

# Entry widget for URL
entry2 = ctk.CTkEntry(root, placeholder_text="Enter site URL", width=200, font=("Arial", 14))
entry2.pack(pady=0)

# Generate button
button = ctk.CTkButton(root, text="Generate", width=200, command=generate)
button.pack(pady=10)

# Set window size
root.geometry("400x300")

# Run the application
root.mainloop()
