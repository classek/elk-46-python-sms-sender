import requests
import base64
import tkinter as tk
from tkinter import IntVar, StringVar

def send_sms():
    # Get the username, password, message, phone number, and sender name
    username = username_entry.get()
    password = password_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    phone_number = phone_entry.get()
    sender_name = sender_entry.get()

    payload = {
            'to': phone_number,
            'from': sender_name,
            'message': message,
    }

    if flashsms_var.get():
        payload['flashsms'] = 'yes'
    if dryrun_var.get():
        payload['dryrun'] = 'yes'

    # Build the URL with selected options
    url = f"https://api.46elks.com/a1/sms"

    response = requests.post(url, data=payload, auth=(username, password))

    result_label.config(text=response.text)

# Create the main window
root = tk.Tk()
root.title("46elks SMS Sender")

# Checkbox variables
flashsms_var = IntVar()
dryrun_var = IntVar()

# Entry variables
username_var = StringVar()
password_var = StringVar()
phone_var = StringVar()
sender_var = StringVar()

# Create and place widgets
flashsms_checkbox = tk.Checkbutton(root, text="Flash SMS", variable=flashsms_var)
flashsms_checkbox.grid(row=0, column=0, padx=10, pady=10)

dryrun_checkbox = tk.Checkbutton(root, text="Dry Run", variable=dryrun_var)
dryrun_checkbox.grid(row=0, column=1, padx=10, pady=10)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(root, textvariable=username_var)
username_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=3, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root, textvariable=phone_var)
phone_entry.grid(row=3, column=1, padx=10, pady=10)

sender_label = tk.Label(root, text="Sender Name:")
sender_label.grid(row=4, column=0, padx=10, pady=10)
sender_entry = tk.Entry(root, textvariable=sender_var)
sender_entry.grid(row=4, column=1, padx=10, pady=10)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=5, column=0, padx=10, pady=10)
message_text = tk.Text(root, height=4, width=30)
message_text.grid(row=5, column=1, padx=10, pady=10)

send_button = tk.Button(root, text="Send SMS", command=send_sms)
send_button.grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
