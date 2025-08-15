# 🚀 Flask + MongoDB Atlas Application

> **Author:** Shubham Saini  
> **Date:** August 16, 2025

A modern Flask web app with MongoDB Atlas integration. Features a responsive frontend form and a RESTful API endpoint, ideal for demonstrating full-stack basics with Python and cloud databases.

---

## 📑 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Running the Application](#running-the-application)
7. [Requirements](#requirements)


---

## 📌 Overview

This project is a simple, full-stack Flask web application integrated with **MongoDB Atlas**.  
It includes:

- A RESTful API endpoint (`/api`) that serves data from a backend `data.json` file.
- A modern HTML frontend form for user data (Name & Email) submission, stored securely in MongoDB Atlas.

---

## ✨ Features

- **API Endpoint (`/api`)**  
  Returns the contents of `data.json` as JSON via HTTP GET.

- **Frontend Form**  
  Submits Name & Email.  
  - If the email already exists: shows a friendly error message (no redirect).
  - If successful: redirects to a success page.

---

## 🛠 Technologies Used

- **Python 3.x**
- **Flask** (Web Framework)
- **MongoDB Atlas** (Cloud Database)
- **HTML & CSS** (Frontend form)
- **pymongo, dnspython** (Database & DNS drivers)

---

## 📂 Project Structure

```
.
├── app.py              # Main Flask application
├── templates/
│   ├── form.html       # Form page
│   ├── success.html    # Success message page
│   ├── error.html      # Error message page
├── data.json           # Backend data for /api endpoint
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙ Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/shubham-saini18/Assignment-3
cd /Assignment-3
```

2️⃣ **(Optional) Create and activate a virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

1️⃣ **Configure MongoDB Atlas**  
Edit your `app.py`:
```python
client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/")
```

2️⃣ **Start the Flask server**
```bash
python app.py
```

3️⃣ **Access in your browser:**
- **Form page:** [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- **API endpoint:** [http://127.0.0.1:5000/api](http://127.0.0.1:5000/api)

---

## 📦 Requirements

```
Flask==3.0.3
pymongo==4.9.1
dnspython==2.6.1
```

---


> Crafted for learning and rapid prototyping.  
> Questions or improvements? Feel free to open an issue or submit a pull request!
