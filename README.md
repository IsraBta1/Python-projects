# Python-projects
Development and completion of projects carried out at BYU-Idaho.

# 🐍 Python Projects & Logic Practicing Portfolio (CSE 111)

Welcome to my Python development repository! This space consolidates the core projects, software engineering solutions, and logic exercises developed throughout the **CSE 111 (Programming with Functions)** course at **BYU-Pathway Worldwide / BYU-Idaho**.

The primary purpose of this repository is to showcase proficiency in modular software architecture, data stream manipulation, and advanced automated testing implementation.

---

## 🧠 Logic Practice Tasks (Homeworks)
In addition to the main applications, this repository contains practice scripts specifically designed to reinforce algorithmic thinking and complex problem-solving skills:
* **`words.py` & `test_words.py`:** Advanced text analysis tools to perform string pattern matching and precise common prefix/suffix extraction.
* **`random_numbers.py`:** Structured practices covering memory mutability, optional parameters, and the behavior of lists passed by reference.

---

## 🚀 Weekly Real-World Core Applications

### 🛒 Week 1: Commercial Automation (`app_discount.py` & `time_volume.py`)
* **Dynamic Point of Sale:** A terminal checkout loop that computes exact order totals, handles a 6% tax rate, and grants a 10% discount conditionally based on live calendar days (`datetime`).
* **Automotive Engineering Tool:** Applies complex algebraic formulas using `math.pi` to calculate tire capacity in liters, leveraging File I/O for persistent audit logs in `volumes.txt`.

### 🛡️ Week 2: Security & Cryptography (`password.py`)
* **Password Strength Analyzer:** A metric scoring system (0 to 5) that vets user inputs against standard wordlists and leaked password databases (`toppasswords.txt`). It implements length-dominance logic and entropy criteria using `any()`.

### 🌤️ Week 3: Environmental Calibration & QA (`weather.py`)
* **Thermal Unit Converter:** A precision utility transforming Fahrenheit into Celsius.
* **Quality Assurance (QA):** Complete testing suite utilizing `pytest.approx` to bypass standard floating-point binary representation errors, ensuring absolute arithmetic accuracy.

### 🧪 Week 4: Scientific Data Structures (`chemistry.py`)
* **Molar Mass Calculator:** Leverages a Python dictionary as a high-performance Hash Map ($O(1)$ lookup time) to store periodic table attributes, parsing chemical formulas through multi-dimensional list unpacking.

### 🧾 Week 5: Fault-Tolerant Systems & Auditing (`receipt.py`)
* **Advanced Retail Transaction Processor:** An automated batch order management system that parses CSV data feeds.
* **Professional Enhancements:** Comprehensive exception handling (`KeyError`, `FileNotFoundError`), an interactive manual checkout feature, and a secure transaction archiving system with chronological time-stamped log files.

---

## 🧪 Running the Automated Testing Suite (Pytest)
To execute the quality control assertions across all software components and logic homeworks simultaneously, run the following commands in your terminal:

```bash
pip install pytest
pytest
