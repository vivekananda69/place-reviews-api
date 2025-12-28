# 📍 Place Reviews REST API

A **production-quality REST API** built using **Django** and **Django REST Framework** that allows authenticated users to review places such as shops, doctors, restaurants, etc.

This project focuses on **clean data modeling**, **correct API design**, and **edge-case handling**, rather than excessive features.

---

## 🧠 Problem Overview

The API allows users to:

* Register using **phone number**
* Authenticate using **token-based authentication**
* Add reviews for places
* Search places by name and rating
* View place details with reviews

There is **no public access** — all APIs require authentication.

---

## 🧠 Assumptions

* Each user registers using a **unique phone number**
* A user can review a place **only once**
* A place is uniquely identified by **(name, address)**
* All APIs require authentication (except registration)
* No third-party services are used
* SQLite is used for simplicity and portability

---

## ⚙️ Tech Stack

* Python 3
* Django
* Django REST Framework
* SQLite
* Token Authentication

---

## 🚀 Project Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/place-reviews-api.git
cd place-reviews-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework
```

---

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Start Server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

This API uses **Token Authentication**.

Include the token in request headers:

```
Authorization: Token <your_token>
```

---

## 📌 API Endpoints

---

### 1️⃣ Register User

**POST** `/register/`

Request Body:

```json
{
  "phone": "9999999999",
  "name": "John Doe",
  "password": "password123"
}
```

Response:

```json
{
  "message": "User registered successfully",
  "token": "<auth_token>"
}
```

---

### 2️⃣ Add Review (Authenticated)

**POST** `/review/`

Request Body:

```json
{
  "name": "Shop1",
  "address": "Street1",
  "rating": 5,
  "text": "Excellent service"
}
```

Rules:

* One review per user per place
* Duplicate reviews are rejected

---

### 3️⃣ Search Places

**GET** `/search/?name=Shop&min_rating=4`

Features:

* Exact name matches shown first
* Partial name search supported
* Filter by minimum average rating

---

### 4️⃣ Place Detail View

**GET** `/place/<place_id>/`

Returns:

* Place name and address
* Average rating
* All reviews
* **Current user’s review is shown first**

---

## 🧪 Data Population Script

A helper script is included to generate sample data quickly.

### 📍 Location

```
scripts/populate_data.py
```

### ▶️ Run Script

```bash
python manage.py shell
```

```python
from scripts.populate_data import run
run()
```

This creates:

* 5 users
* 5 places
* 15 reviews

---

## ✅ Key Highlights

* Custom user model with **phone-based authentication**
* Strong database constraints to prevent duplicates
* Clean API structure
* Proper error handling
* Realistic test data
* Ready for frontend integration

---

## 📦 Submission Notes

* No unnecessary dependencies
* Clean and readable codebase
* SQLite database excluded from repository
* Suitable for production extension

---

## 🏁 Conclusion

This project demonstrates **backend fundamentals**, **REST API design**, and **real-world Django practices** with a strong emphasis on correctness and clarity.

---
