# 🚀 travel_lykke2

A Django-based Travel Booking Web Application (assignment project).  
Backend: **Python (Django)**  
Database: **MySQL** (with SQLite fallback for local testing)  
Frontend: **Bootstrap 5** (responsive & mobile-friendly)

---

## ✨ Features
- User registration/login/logout  
- User profile with phone & city  
- Travel options: Flight, Train, Bus  
- Filter by type, source, destination, date  
- Booking with seat availability check  
- Cancel bookings (seats restored)  
- Admin panel to manage Travel Options & Bookings  
- Responsive design (Bootstrap 5)

---

## ⚙️ Local Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/travel_lykke2.git
cd travel_lykke2
```

### 2. Create virtual environment & install requirements
```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Database setup
#### Option A: MySQL (recommended)
Edit **travel_lykke2/settings.py**:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_lykke2_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

#### Option B: SQLite (quick local testing)  
Uncomment the SQLite section in settings.

### 4. Migrate DB & create superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run server
```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---


## 🔑 Admin Panel
- URL: `/admin/`  
- Use the superuser credentials created earlier.  
- Add `TravelOption` entries (flights, trains, buses).

---

## 📌 Notes
- Default DB in settings is **MySQL**, switch to SQLite for local testing.  
- For production, always **disable DEBUG** and **use strong SECRET_KEY**.  
- Extend with payments, email confirmations, etc. if needed.  
