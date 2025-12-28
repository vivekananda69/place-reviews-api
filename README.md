```markdown
# Place Reviews REST API

A production-quality REST API built using **Django** and **Django REST Framework** that allows authenticated users to review places such as shops, doctors, restaurants, etc.

This project focuses on **clean data modeling**, **correct API design**, and **real-world deployment**, rather than excessive features.

---

## 🌐 Live Demo

### 🔹 Backend API (Render)
https://place-reviews-api.onrender.com

Example:
```

GET /search/

````

### 🔹 Demo UI (Streamlit)
https://appapppy-zlpvvb3ten8jzfyzxipwty.streamlit.app/

The Streamlit UI is provided **only for demonstration** and consumes the same REST APIs used by any frontend or mobile app.

---

## 🧠 Assumptions

- All APIs require authentication except user registration and place search
- Users register using a **unique phone number**
- A user can review a place **only once**
- A place is uniquely identified by **(name, address)**
- No third-party services are used
- SQLite is used for simplicity (for demo/assignment purposes)

---

## ⚙️ Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite
- Token Authentication
- Streamlit (demo UI)
- Render (deployment)

---

## 🚀 Project Setup (Local)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
````

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Authentication

Token-based authentication is used.

Include the token in request headers:

```
Authorization: Token <your_token>
```

---

## 📌 API Endpoints

### 1️⃣ Register User

**POST** `/register/`

```json
{
  "phone": "9999999999",
  "name": "John Doe",
  "password": "password123"
}
```

---

### 2️⃣ Add Review (Authenticated)

**POST** `/review/`

```json
{
  "name": "Shop1",
  "address": "Street1",
  "rating": 5,
  "text": "Great service"
}
```

Rules:

* One review per user per place
* Duplicate reviews are blocked

---

### 3️⃣ Search Places

**GET** `/search/?name=Shop&min_rating=4`

Features:

* Exact match prioritization
* Partial search support
* Filter by minimum rating

---

### 4️⃣ Place Detail

**GET** `/place/<place_id>/`

Returns:

* Place details
* Average rating
* All reviews
* Current user’s review shown first

---

## 🎨 Demo UI (Streamlit)

A lightweight Streamlit UI is included for demonstration.

```bash
streamlit run streamlit_app.py
```

The UI interacts only with the REST APIs and does not contain any backend logic.

---

## 📦 Deployment Notes

* Backend deployed on **Render**
* Streamlit UI deployed on **Streamlit Community Cloud**
* Database is SQLite (non-persistent on redeploy)
* For production use, PostgreSQL would be preferred

---

## ✅ Key Highlights

* Custom user model with phone-based login
* Proper database constraints
* Clean API design
* Real deployment experience
* Clear separation of backend and UI

---

## 🏁 Conclusion

This project demonstrates backend fundamentals, REST API design, authentication, and real-world deployment using Django.

````

---

👉 Commit README:

```bash
git add README.md
git commit -m "Update README with live deployment and demo links"
git push
````
