# Personal Expense Tracker (CLI)

A simple command-line Python application to track personal expenses.
Users can add expenses, view them in a table, and see spending summaries.

---

## Features

* Add expenses (amount, category, description)
* View all expenses in a table
* Calculate total spending
* Show category-wise spending summary
* Save expenses to a JSON file
* Load saved data when the program restarts

---

## Project Structure

expense-tracker
│
├── src/
│   ├── main.py
│   ├── tracker.py
│   └── storage.py
│
├── README.md
└── .gitignore

---

## Setup

### 1. Create Virtual Environment

```
python -m venv venv
```

### 2. Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

Mac / Linux:

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install tabulate
```

---

## Run the Application

```
python src/main.py
```

---

## Author

Purushotham Reddy
