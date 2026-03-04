# Personal Expense Tracker (CLI)

A simple command-line application built with Python to track personal expenses.

## Features

* Add expenses (amount, category, description)
* View all expenses in a table
* Calculate total spending
* Category-wise expense summary
* Saves data to JSON
* Loads saved data automatically when the program restarts

## Project Structure

expense-tracker
│
├── src
│   ├── main.py
│   ├── tracker.py
│   └── storage.py
│
├── README.md
└── .gitignore

## Setup

### 1. Create virtual environment

```
python -m venv .venv
```

### 2. Activate virtual environment

Windows:

```
.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install tabulate
```

## Run the application

```
python src/main.py
```

## Author

Purushotham Reddy
