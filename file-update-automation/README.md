Access Control List Update Automation (Python)
Project Description

This project is a self-directed experimental cybersecurity automation exercise designed to simulate how access control lists (ACLs) can be programmatically managed.

In this scenario, an allow list of approved IP addresses is stored in a file named:allow_list.txt
A separate remove list contains IP addresses that should no longer be granted access.

The purpose of this project is to design and implement a Python algorithm that:

Reads the allow list file

Identifies IP addresses that must be removed

Updates the file securely

Ensures unauthorized IPs are automatically revoked
The steps I took
Step 1 — Assign the File Name to a Variable: import_file = "allow_list.txt"
Step 2 — Open the File in Read Mode : with open(import_file, "r") as file:
Step 3 — Read the File Contents : ip_addresses = file.read()
Step 4 — Convert the String into a List : ip_addresses = ip_addresses.split()
Step 5 — Define the Remove List : remove_list = ["192.168.1.10", "10.0.0.5"]
Step 6 — Iterate Through the Remove List : for element in remove_list:
Step 7 — Validate Before Removing : if element in ip_addresses:
Step 8 — Remove the Unauthorized IP : ip_addresses.remove(element)
Step 9 — Convert the Updated List Back Into a String : ip_addresses = "\n".join(ip_addresses)
Step 10 — Rewrite the File With Updated Data : with open(import_file, "w") as file: file.write(ip_addresses)
Complete Algorithm
import_file = "allow_list.txt"

remove_list = ["192.168.1.10", "10.0.0.5"]

with open(import_file, "r") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
