# 🍽️ Online Restaurant Booking System

## 📌 Overview
The **Online Restaurant Booking System** is a web-based application built using Django that allows users to browse restaurants and make table reservations online. It also provides functionality for restaurant owners to register and manage their listings.

## 🚀 Features
### 👤 User Features
* User registration and login
* Browse available restaurants
* View restaurant details (images, info, etc.)
* Book tables online
* View booking status
* Cancel bookings

### 🍴 Restaurant Features
* Restaurant registration
* Upload restaurant details and images
* Manage bookings

### 🔐 Authentication
* Role-based login system (Customer / Restaurant)

## 🛠️ Tech Stack
* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Django Templates
* **Database:** SQLite3
* **Media Handling:** Django Media Files
* **Static Files:** CSS, Images

## ⚙️ Setup & Installation
### 1️⃣ Clone the Repository
* Frok the Repository
```bash
git clone <your-repository-link>
cd <project-folder>
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv env
```

Activate the environment:
**Windows:**
```bash
env\Scripts\activate
```

**Mac/Linux:**
```bash
source env/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install django
pip install pillow
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Project
```bash
python manage.py runserver
```

Then open your browser and go to:
```
http://127.0.0.1:8000/
```

## ⚠️ Note
All data used in this project is **fake** and created only for **experimental and educational purposes**.

## 📌 Future Improvements
* Payment integration
* Email notifications
* Advanced search & filters
* Ratings & reviews system
* Admin dashboard improvements

## 👨‍💻 Author
Niket Aggarwal
<br/>
Aunranjan Toppo

## 📄 License
This project is for educational purposes.
(As a College Backend Project)
