# Automated WhatsApp Birthday Wisher
The Automated WhatsApp Birthday Wishes project is a Python script that uses the Selenium WebDriver to automate the process of sending birthday wishes to your friends and family on WhatsApp. The script reads a CSV file named "birthdays.csv" to determine whose birthdays are coming up, and sends personalized messages to each person on their special day. The script is designed to run on your local machine and interact with the WhatsApp Web interface.

# Requirements

To run the script, you will need the following:

*Python 3.x
*Selenium WebDriver for chrome 
*A WhatsApp account

# Installation

To get started, clone this repository to your local machine:

`git clone https://github.com/saleha-muzammil/auto-birthday-wisher-whatsapp.git`

Next, install the required Python modules:

`pip install selenium`

Finally, download and install the ChromeDriver for Selenium from here:
https://sites.google.com/a/chromium.org/chromedriver/downloads

Usage

To use the script, first update the "birthdays.csv" file with the birthdays of the people you want to wish a happy birthday to. The file should contain one row per person, with the following columns:

*Name (as saved on whatsapp)
*Date of Birth (in format "YYYY-MM-DD")

Once the birthdays are updated, run the script using the following command:

`python3 whatsapp_wisher.py`

The script will automatically check the "birthdays.csv" file and send personalized birthday messages to anyone whose birthday is today. The script will run once per day, so you can set up a cron job or scheduled task to run the script automatically.

# Troubleshooting

If you encounter any issues with the script, check the following:

*Make sure you have installed the required Python modules and Selenium WebDriver for your chosen browser.
*Make sure your WhatsApp account is logged in and connected to WhatsApp Web.
*Double-check that the "birthdays.csv" file is formatted correctly and contains the correct information and is stored in the same directory as whatsapp_wisher.py

If you still encounter issues, feel free to open an issue in the repository.

# Credits

This project was created by me, Saleha Muzammil.




