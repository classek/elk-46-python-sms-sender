46elks SMS Sender GUI

This Python script provides a graphical user interface (GUI) for sending SMS messages using the 46elks SMS API. 
The GUI is built using the Tkinter library and allows users to input their 46elks credentials, message details, and optional settings.

This requires account and credits on:

https://46elks.com/
or
https://46elks.se/
or
https://46elks.fi/
or
https://46elks.hr/


Features:
Flash SMS Option: Send messages as flash SMS if desired.
Dry Run Option: Test the SMS sending functionality without actually sending an SMS.
User-Friendly Interface: Simple and intuitive GUI for easy interaction.

Usage:
Input your 46elks username, password, recipient's phone number, sender name, and message text.
Optionally select the "Flash SMS" or "Dry Run" checkboxes based on your requirements.
Click the "Send SMS" button to initiate the SMS sending process.
View the result in the provided label.

Requirements:
Python 3.x
Tkinter
Requests library (pip install requests)
How to Run:
Clone the repository or download the script.
Install the required libraries using pip install -r requirements.txt.
Run the script with python sms_sender_gui.py.
