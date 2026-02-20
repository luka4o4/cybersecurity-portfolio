# Log4j Exploitation & Ransomware Recovery Simulation

## Project Overview

This project simulates a ransomware incident resulting from exploitation of a Log4j vulnerability in a controlled lab environment.

The goal of this exercise was to:

- Understand how Log4j vulnerabilities can lead to remote code execution
- Observe how ransomware can encrypt sensitive files
- Practice post-exploitation recovery techniques
- Develop automation to recover encrypted data

⚠️ All testing was conducted in a local lab environment for educational purposes only.

---

## Scenario Summary

A vulnerable Log4j application was exploited, leading to a simulated ransomware attack.

The ransomware encrypted a sensitive archive file (`enc.zip`), preventing access to its contents.

The objective was to recover the encrypted archive using a password brute-force approach.

---

## Recovery Method

A Python script was developed to perform a dictionary-based brute-force attack against the encrypted ZIP file using the `rockyou.txt` wordlist.

The script attempts each password in the list until the correct one is found.

---

## Python Brute-Force Script

```python
from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        print(f"[+] Password found: {password.decode().strip()}")
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")

    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    break
            else:
                print("[!] Password not found in list")

if __name__ == "__main__":
    main()
