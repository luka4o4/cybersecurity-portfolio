# Brute Force Attack Simulation Using Hydra (LabEx)

## 1. Overview

This project documents a brute-force attack simulation performed in a controlled lab environment using Hydra.

The objective was to understand how automated password attacks work and how they can be detected and mitigated from a SOC perspective.

---

## 2. Tools & Environment

- Hydra (THC Hydra)
- Linux Terminal
- Username wordlist
- Password wordlist (500 common passwords)
- Local web server (localhost:8080)

---

## 3. Attack Preparation

A username wordlist was created containing common default accounts:

- admin
- user
- root

Attackers frequently target predictable usernames during brute-force attempts.

---

## 4. Attack Execution

Hydra was configured to test multiple username and password combinations against a login form running locally.

The tool automated authentication attempts using:

- A list of potential usernames
- A list of commonly used weak passwords

Successful credentials were written to an output file for review.

---

## 5. Results & Findings

The simulation demonstrated:

- Weak passwords can be cracked quickly.
- Automation significantly increases attack speed.
- Default usernames increase exposure risk.

---

## 6. SOC Detection Perspective

This type of activity would generate:

- High volumes of failed login attempts
- Repeated authentication attempts on specific accounts
- Potential account lockout events

Detection strategies include:

- Monitoring authentication logs
- Implementing rate limiting
- Enforcing strong password policies
- Enabling Multi-Factor Authentication (MFA)

---

## 7. Conclusion

This lab reinforced the importance of strong authentication controls and proactive monitoring.

Understanding offensive tools improves defensive detection capabilities in a Security Operations Center (SOC) environment.
