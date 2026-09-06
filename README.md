# 🔐 Password Strength Analyzer

A lightweight Python CLI tool for **password strength validation and secure password generation**.

## Features

* 🔎 Password strength validation
* 🔑 Secure password generation
* 🔤 Uppercase and lowercase character validation
* 🔢 Number validation
* 🔣 Special character validation
* 📏 Minimum password length validation
* 🛡️ Cryptographically secure random generation using Python `secrets`

## Requirements

* Python 3.x
* No external dependencies

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/password-strength-analyzer.git
cd password-strength-analyzer
python3 script.py
```

## Usage

```text
[1] Analyze a password
[2] Generate a strong password
[3] Exit
```

### Password Analysis

Checks whether a password contains:

* At least 8 characters
* Uppercase letter
* Lowercase letter
* Number
* Special character

### Password Generation

Generates passwords using Python's `secrets` module and securely randomizes their characters.

## Technologies

* Python 3
* Regular Expressions (`re`)
* Secure Random Generation (`secrets`)
* Git & GitHub

## Purpose

This project was developed as a practical cybersecurity exercise to explore **password security, input validation, regular expressions, and secure random generation**.

## Future Improvements

* Password strength scoring
* Entropy calculation
* Common password detection
* Passphrase generation
* Unit testing
* Improved CLI interface

## Disclaimer

Educational project. It is not intended to replace professional password-security solutions.


