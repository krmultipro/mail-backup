# 📩 Email Backup Script - Save Your Gmail Emails Locally

## 🔹 Introduction
This Python script **automatically downloads all your Gmail emails** and saves them in an `.mbox` file, which can be used to restore your emails later.

✅ **No personal data is shared** - everything runs on your local machine.  
✅ **Simple configuration** - just enter your email credentials in `config.json`.  
✅ **Compatible with Gmail.**

---

## 🔹 Step 1: Install Python
Make sure you have **Python 3** installed. If not, download it here:  
[Download Python](https://www.python.org/downloads/)

---

## 🔹 Step 2: Install Required Packages
After downloading the script, open a terminal (Command Prompt on Windows) and navigate to the script folder. Then, run: pip install -r requirements.txt


This installs all necessary dependencies.

---

## 🔹 Step 3: Configure Your Email Credentials
1. Open the `config.json` file.
2. Replace:
   - `"email"` → Your **Gmail address**
   - `"password"` → Your **App Password** (see below).

💡 **Important:** You must use a **Google App Password**, not your regular Gmail password.

### How to Generate a Google App Password:
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Under "Signing in to Google," click **App Passwords**.
3. Generate a new password for "Mail" → **IMAP**.
4. Copy and paste it into `config.json`.

---

## 🔹 Step 4: Run the Script
To start backing up your emails, open a terminal and run: python3 mail_backup.py

This will:
✅ Connect to your Gmail account.  
✅ Download all emails and save them in `backup_gmail.mbox`.  
✅ Show real-time progress.  

---

## 🔹 Step 5: Access Your Backup
The script creates a file called **`backup_gmail.mbox`**, which contains all your emails.

You can open this file with:
📂 **Thunderbird** (Import via "ImportExportTools NG").  
📂 **MBOX viewers** (like [Mbox Viewer](https://www.freeviewer.org/mbox/)).  

---

## 🔹 Notes
- This script **only works with Gmail**.
- **No emails will be deleted** from your account.

---

## 🔹 Support
If you have any issues, feel free to message me on Fiverr! 😊

