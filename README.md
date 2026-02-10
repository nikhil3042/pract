# 🧪 Test Automation Framework -- Setup & Execution Guide

Welcome! This guide will help you set up the framework and run tests
step-by-step.\


------------------------------------------------------------------------

## 📦 Prerequisites

Make sure you have installed:

-   🐍 Python (3.8 or higher)
-   🌐 Google Chrome / Microsoft Edge
-   📦 pip (comes with Python)
-   🧪 pytest\
-   📊 Allure (for reporting)

------------------------------------------------------------------------

# ⚙️ Project Setup

## 1️⃣ Create Virtual Environment (venv)

Create an isolated environment for dependencies.

``` bash
python -m venv venv
```

------------------------------------------------------------------------

## 2️⃣ Activate Virtual Environment

### ▶️ Windows

``` bash
venv\Scripts\activate
```

You'll see `(venv)` appear in your terminal once activated ✅

------------------------------------------------------------------------

## 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# 🧪 Running Tests

## ▶️ Run all tests (Default: Chrome)

``` bash
pytest
```

✔ Runs all test cases\
✔ Launches Chrome browser by default

------------------------------------------------------------------------

## 🌐 Run tests on Chrome

``` bash
pytest --browser='chrome'
```

------------------------------------------------------------------------

## 🌐 Run tests on Edge

``` bash
pytest --browser='edge'
```

------------------------------------------------------------------------
## 📊 View Allure Report

``` bash
allure serve reports/allure-results
```

✔ Opens interactive Allure dashboard in browser\
✔ Shows: - Test steps - Failures - Screenshots - Logs

------------------------------------------------------------------------

# 🗂️ Project Commands Summary

  ---------------------------------------------------------------------------------------------
  🔹 Action                         💻 Command
  --------------------------------- -----------------------------------------------------------
  Create venv                       `python -m venv venv`

  Activate venv                     `venv\Scripts\activate`

  Run tests (default Chrome)        `pytest`

  Run tests on Chrome               `pytest --browser='chrome'`

  Run tests on Edge                 `pytest --browser='edge'`

  Generate Allure results           `pytest --alluredir=reports/allure-results`

  View Allure report                `allure serve reports/allure-results`
  
  Generate HTML report              `pytest --html=reports/report.html --self-contained-html`
  
---------------------------------------------------------------------------------------------
