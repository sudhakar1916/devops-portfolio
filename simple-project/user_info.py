# ================================================
# Simple Python Script: User Info Collector + Save
# Collects: Name, Role, Age, Email, Phone
# Displays formatted output
# Automatically saves to BOTH JSON and CSV files
# (Appends new records each time you run it)
# ================================================

import json
import csv
import os
from datetime import datetime

# Get inputs from user
name  = input("Enter your Name     : ").strip()
role  = input("Enter your Role     : ").strip()
age   = input("Enter your Age      : ").strip()
email = input("Enter your Email    : ").strip()
phone = input("Enter your Phone    : ").strip()

# Basic validation
if not name or not role or not age or not email or not phone:
    print("\n❌ Error: All fields are required!")
    exit()

# Formatted output
print("\n" + "=" * 60)
print(" " * 20 + "👤 USER INFORMATION")
print("=" * 60)
print(f"{'Name':<15} : {name}")
print(f"{'Role':<15} : {role}")
print(f"{'Age':<15} : {age} years")
print(f"{'Email':<15} : {email}")
print(f"{'Phone':<15} : {phone}")
print("=" * 60)

# Prepare data with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user_data = {
    "Name": name,
    "Role": role,
    "Age": age,
    "Email": email,
    "Phone": phone,
    "Timestamp": timestamp
}

# ====================== SAVE TO JSON ======================
json_file = "user_data.json"

# Load existing data if file exists, else start fresh
if os.path.exists(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data_list = json.load(f)
else:
    data_list = []

data_list.append(user_data)

# Write back
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=4)

# ====================== SAVE TO CSV ======================
csv_file = "user_data.csv"
file_exists = os.path.exists(csv_file)

with open(csv_file, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=user_data.keys())
    if not file_exists:
        writer.writeheader()      # Write header only once
    writer.writerow(user_data)

# ====================== CONFIRMATION ======================
print("✅ Thank you! All data collected and saved successfully.")
print(f"💾 Files created/updated in the current folder:")
print(f"   📄 {json_file}  ← JSON format (best for programs)")
print(f"   📊 {csv_file}   ← CSV format (opens in Excel/Google Sheets)")
