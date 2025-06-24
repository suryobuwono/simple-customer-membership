# Python Project: A Simple Customer Membership Management System

A simple Python-based customer membership management system designed for a fictional e-commerce service called **PacCommerce**. PacCommerce offers three membership tiers — **Platinum**, **Gold**, and **Silver** — each with its own unique benefits and requirements. This program includes functionality for storing a member database, displaying benefits, checking requirements, automatically predicting membership tiers using Euclidean distance, verifying user identities, calculating price discounts, and providing admin-level access for user management.

---

## Objectives

### Learning Objectives
- Demonstrate proficiency in using **object-oriented programming (OOP)** to create a Python program.
- Apply **clean coding practices** following **PEP8 guidelines**.
- Showcase **logical and systematic thinking** in problem-solving using Python.

### Program Features

#### User Features
- `Membership()` → Includes an **identity verification** feature  
  Ensures no duplicate user entries and protects data integrity by verifying re-entry of users who were already listed in the database before the program ran.
- `show_benefit()` → Displays benefit descriptions and discount rates for each membership tier.
- `show_requirements()` → Displays monthly income and expense requirements for each tier.
- `predict_membership()` → Automatically assigns a membership tier based on the user's monthly income and expenses using Euclidean distance calculation.
- `show_membership()` → Displays the user's current membership status.
- `calculate_price()` → Calculates the total price after applying the appropriate membership-based discount.

#### Admin Features
- `show_all_members()` → Displays all registered members (password protected).
- `remove_member()` → Removes a member from the database (password protected).

---

## Tools Used

- **Language**: Python 3  
- **Built-in Modules**:
  - [`tabulate`](https://pypi.org/project/tabulate/) – For clean table display  
  - [`math`](https://docs.python.org/3/library/math.html) – Used for Euclidean distance calculation

---

## Program Description

### 1. `paccommerce.py`
This Python script implements the core customer membership system for PacCommerce. Both users and admins can access all key features mentioned above through this class-based implementation.

### 2. `test_case_paccommerce.ipynb`
This Jupyter Notebook contains structured test cases to validate the `paccommerce.py` script. It simulates real-world user scenarios and interactions with the membership system, including:

- Viewing membership benefits and requirements
- Predicting the user's membership tier based on income and expenses
- Verifying returning users through identity checks
- Calculating discounted shopping totals
- Admin access to view and remove members securely

---

## How to Run the Program

1. Download both `paccommerce.py` and `test_case_paccommerce.ipynb` to your local directory.
2. Open the notebook file (`.ipynb`) using **Jupyter Notebook** or **VSCode** (with the Jupyter extension).
3. Ensure the `paccommerce.py` script is in the **same directory** or is properly imported.
4. Run the notebook cells step by step to explore and test all functionalities.
