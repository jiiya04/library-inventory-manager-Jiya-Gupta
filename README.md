# Library Inventory Manager

This is a Python project that manages a small library of books.  
It allows adding books, issuing and returning them, searching books, and saving the catalog in a JSON file.



## Project Features
- Book class with title, author, ISBN, and status  
- LibraryInventory class to add, search, issue, return, and display books  
- Data saved in `data/catalog.json` using JSON  
- Menu-driven CLI (`cli/main.py`)  
- Basic error handling and logging  
- Proper folder structure with Python packages



## Folder Structure
library_manager/
book.py
inventory.py
cli/
main.py
data/
catalog.json
README.md
requirements.txt



## How to Run
Open terminal in the project folder and run:
python -m cli.main

## Requirements
This project uses only Python's built-in modules:
- json  
- pathlib  
- logging  
- dataclasses  

No external installations required.
