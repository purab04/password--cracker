# 🔐 Password Cracker (Internship Project)

**By Purab Awasthi**  
**Intern ID: ITID0485**  
**Organization: Inlighn Tech**

## 📌 Objective

This project demonstrates how to crack hashed passwords using Python, employing **dictionary attacks** and **brute-force techniques**. It serves as an educational tool for understanding:

- Cryptographic hash functions
- Password security vulnerabilities
- Multi-threading in Python
- Command-line interfaces

## 🚀 Features

- Supports `MD5`, `SHA-1`, and `SHA-256` hash algorithms
- Dictionary attack using custom wordlists
- Brute-force attack with adjustable length and character sets
- Multi-threading for improved performance
- CLI interface using `argparse`

## 📄 Files

- `password_cracker.py`: Main Python script
- `password_cracker_internship_project_purab.pdf`: Full project report with explanation, code, and usage

## 🛠️ Usage

```bash
# Dictionary Attack
python password_cracker.py <hash> md5 --wordlist wordlist.txt

# Brute-force Attack
python password_cracker.py <hash> sha256 --min 1 --max 4 --charset abc123 --threads 4
