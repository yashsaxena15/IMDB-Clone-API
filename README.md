# 🎬 IMDb Clone – Backend REST API

This project is a **backend REST API** for an IMDb-like movie review platform, built using **Django** and **Django REST Framework (DRF)**.  
It focuses on **authentication, database relationships, business logic, and API design**, without a frontend.

The API can be consumed by any frontend (React, mobile apps, etc.) or tested using tools like **Postman**.

---

## 🚀 Features

- User authentication using **Token-based Authentication**
- CRUD APIs for:
  - Streaming Platforms
  - Watchlists (Movies)
  - Reviews
- One-to-many and many-to-one database relationships
- Users can review a movie **only once**
- Dynamic calculation of average movie ratings
- Role-based access control:
  - Admins can manage platforms and movies
  - Users can create/update their own reviews
- API throttling to prevent abuse
- Pagination for large datasets
- Filtering and ordering support

---

## 🛠 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **MySQL**
- **DRF Token Authentication**

---

## 📂 Database Models

### StreamPlatform
Represents streaming platforms like Netflix, Prime Video, etc.

- Name
- Description
- Website

---

### WatchList
Represents movies or shows available on a platform.

- Title
- Storyline
- Platform (Foreign Key)
- Active status
- Average rating
- Number of ratings
- Created timestamp

---

### Review
Represents user reviews for movies.

- User (Foreign Key)
- Movie (Foreign Key)
- Rating (1–5)
- Review description
- Created & updated timestamps

---

## 🔐 Authentication & Permissions

- Token-based authentication using **DRF Authtoken**
- Only authenticated users can create reviews
- Custom permission classes:
  - **IsAdminOrReadOnly** – Admins can modify, others can only read
  - **IsReviewUserOrReadOnly** – Users can update/delete only their own reviews

---

## 📌 API Endpoints (Sample)

### Authentication
- `POST /account/register/` – User registration
- `POST /account/login/` – Get auth token
- `POST /account/logout/` – Logout user

---

### Platforms & Movies
- `GET /watch/platformlist/` – List streaming platforms
- `GET /watch/watchlist/` – List movies
- `GET /watch/watchlist/<id>/` – Movie details

---

### Reviews
- `POST /watch/<movie_id>/review-create/` – Create a review
- `GET /watch/<movie_id>/review/` – List reviews for a movie
- `PUT /watch/review/<id>/` – Update a review
- `DELETE /watch/review/<id>/` – Delete a review

---

## ⚙️ Advanced DRF Features Used

- Generic class-based views
- ModelViewSets & Routers
- Custom permissions
- Throttling (Anon & User based)
- Pagination
- Filtering and ordering
- Nested serializers

---

## 🧠 Business Logic Highlights

- Prevents duplicate reviews by the same user for a movie
- Automatically updates movie rating statistics
- Enforces role-based API access
- Clean separation of concerns using serializers and views

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

git clone <your-repo-url>
### 2️⃣ Create and activate virtual environment

python -m venv env
source env/bin/activate
### 3️⃣ Install dependencies

pip install -r requirements.txt
### 4️⃣ Configure MySQL database
Update database credentials in settings.py.

### 5️⃣ Run migrations

python manage.py makemigrations
python manage.py migrate
### 6️⃣ Start the server

python manage.py runserver

## 🧪 Testing the API

- You can test all endpoints using:

- Postman

- cURL

- Any frontend client

All responses are returned in JSON format.

## 📌 Notes

- This project focuses only on backend functionality.

- Frontend and deployment are not included.

- Designed primarily for learning and backend interview preparation.

## ✨ Future Improvements

- Improve rating calculation using weighted averages

- Add JWT authentication

- Add search APIs

- Deploy on cloud (AWS / Render / Railway)

- Add frontend client

## 👤 Author

Yash Saxena
Backend Developer | Python | Django REST Framework

