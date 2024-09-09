# Automated Email Sender with Task Scheduling
Automated Email Sender with Task Scheduling using Python and cron jobs

## Project Overview
This project demonstrates how to automate the task of sending emails using Python. The email script is scheduled to run periodically using cron jobs (Linux/macOS) or Task Scheduler (Windows).

## Features
- Automatically sends an email to a specified recipient at a set time.
- Uses Python's `smtplib` and Gmail's SMTP server for email delivery.
- Cron job is used to schedule the script to run at specific times.

## Setup Instructions
**Step 1: Python Script to Send Automated Emails**
First, we’ll create a Python script that sends an email using SMTP. You can use Gmail’s SMTP server to handle email sending. 
  We have an already created file (email_scheduler.py) available.


**Step 2: Scheduling the Script Using Cron Job**
On Linux or macOS, you can schedule this Python script using cron. Here’s how:

Open the terminal and type crontab -e to edit the cron jobs.
Add the following line to schedule the Python script to run every day at 10:00 AM:

  ->   0 10 * * * /usr/bin/python3 /path/to/your/email_scheduler.py >> /path/to/your/logfile.log 2>&1

This cron job will:
1. Run the script every day at 10:00 AM.
2. Redirect the output to a log file for tracking success or errors.
3. For Windows, you can use Task Scheduler to run the script on a schedule.

**Step 3: Install dependencies (if needed):**
  ->   pip install smtplib

Update the email_scheduler.py file with your Gmail credentials:
  1. sender_email: Your Gmail address.
  2. receiver_email: The recipient's email address.
  3. password: Your Gmail app password (if 2-factor authentication is enabled).

**For Windows:**
You can use Task Scheduler to run the script at 10:00 AM daily.

1. Open Task Scheduler.
2. Create a new task.
3. Under the Triggers tab, set it to run daily at 10:00 AM.
4. Under the Actions tab, point to the Python script (email_scheduler.py).

**To Download this repo:**
git clone https://github.com/usamaSheikh/Automated-Email-Sender.git

