# Decimal to Octal Converter

This repository contains a simple Python script that converts a decimal number into its octal equivalent. The script reads a decimal number from the user, processes the conversion, and prints the resulting octal value.

## Requirements

- Python 3.x

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone BIL458
   ```
2. **Navigate to the Repository Folder:**
   ```bash
   cd BIL458-HW
   ```
3. **Run the Script:**
   ```bash
   python main.py
   ```
   Replace `<script_name>.py` with the actual file name containing the code.

4. **Follow the Prompt:**
   - When prompted, enter a decimal number.
   - The script will output the corresponding octal representation.

## Code Overview

- **Input:**  
  The program reads a decimal number from the user.

- **Conversion Process:**  
  The script converts the decimal number to octal by:
  - Repeatedly dividing the number by 8.
  - Calculating the remainder.
  - Building the octal number by summing each remainder multiplied by the corresponding power of 10.

- **Output:**  
  The octal number is printed to the console.









