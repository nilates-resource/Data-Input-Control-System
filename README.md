User Registration and Data Validation System
This project is a Python-based utility designed to handle user registration while ensuring data integrity through strict input validation rules. It prevents "dirty data" from entering the system by validating formats before persistent storage.
Key Features
Phone Number Validation: Ensures the input is exactly 11 digits, starts with the "05" prefix, and contains only numeric characters.
Data Type Integrity: Uses isalpha() and isdigit() checks to ensure that names and locations contain only letters, while numbers remain numeric.
Persistent Storage: Validated entries are automatically saved to a .txt file using the Append (a) mode, ensuring existing records are preserved.
Error Handling: Implements while True loops to provide immediate feedback and prompt the user until valid data is provided.

Technical Stack
Language: Python 3.x
Data Structures: Nested Dictionaries for in-memory data management.
File I/O: Text-based persistent storage.

How to Run
Ensure you have Python installed. (I used pycharm)
Download the user_validation.py file.
Run the script via terminal or command prompt:

Bash
python user_validation.py
Follow the on-screen prompts to register users. The data will be saved to kisiler.txt.

Business Logic
In a real-world business environment, cleaning data after it has been collected is costly and time-consuming. This script demonstrates a "Validation at Source" approach, which is critical for maintaining high-quality datasets for further analysis—a key skill for any Management Information Systems (MIS) student.
