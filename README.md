# Library Inventory Management System

This project is a simple library management system created for the Programming for Problem Solving using Python course.

## Features
- Add a new book
- Issue a book
- Return a book
- Search for books by title or ISBN
- View all books
- Data stored in JSON (`books.json`)

## Project Structure
.
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   └── inventory.py
├── cli/
│   └── main.py
├── books.json
├── README.md
├── .gitignore
└── requirements.txt

## How to Run
1. Open Command Prompt
2. Navigate to the project folder
3. Run:

   python -m cli.main

You can also run directly:

   python cli/main.py

## Requirements
This project uses only Python built-in libraries (no external installation needed).
