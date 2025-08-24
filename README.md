# ✧･ﾟ: *✧･ﾟ:* 🚀 77.uz APIs (DRF Project) *:･ﾟ✧*:･ﾟ✧

## 📌 Loyihaning maqsadi

---
    Bu loyiha Django Rest Framework asosida qurilgan bo‘lib,
    foydalanuvchilarni ro‘yxatdan o‘tkazish, login qilish, ma’lumotlarni 
    boshqarish va API orqali ishlash imkoniyatini beradi.
---

## ⚡️ Xususiyatlar

- 🔑 JWT autentifikatsiya
- 👤 Custom User modeli (phone_number orqali login)
- 📍 Address bilan bog‘langan User
- 🖼 Profil rasmi yuklash
- 🛠 DRF asosida API endpointlar
- 📊 JSON, CSV, Excel va PDF formatlarda hisobot chiqarish
---

## 🛠 Texnologiyalar
- Backend: Django, DRF
- Database: PostgreSQL
- Auth: JWT (SimpleJWT)
- Documentation: DRF Spectacular (Swagger & Redoc)
---

## 🌟 API Endpoints  

### 🔐 Accounts  
- `POST /accounts/register/` – 🆕 Yangi foydalanuvchi ro‘yxatdan o‘tish  
- `POST /accounts/login/` – 🔑 Foydalanuvchi login  
- `GET /accounts/me/` – 👤 Foydalanuvchi profili  
- `PUT /accounts/edit/` – ✏️ Profilni yangilash  
- `POST /accounts/token/refresh/` – ♻️ Token yangilash  

---

### 🏬 Store  
- `GET /store/products/` – 📦 Mahsulotlar ro‘yxati  
- `POST /store/products/` – ➕ Yangi mahsulot qo‘shish  
- `GET /store/categories-with-childs/` – 🗂 Kategoriyalar va sub-kategoriyalar  
- `GET /store/my-ads/` – 📢 Mening e’lonlarim  
- `POST /store/my-search/` – 🔍 Qidiruvni saqlash  
- `GET /store/search/populars/` – ⭐ Mashhur qidiruvlar  

---

## ⚙️ Texnologiyalar  
- 🐍 Python 3.13  
- 🌐 Django 5.2  
- 🎯 Django REST Framework  
- 💾 SQLite (development uchun)  

---
## 🎉 Muallif

- 👤 Bunyodjon Mamadaliyev
- 📧 Email: bunyodjon.mamadaliyev.bm@gmail.com
- 📍 Farg‘ona, O‘zbekiston
---
## ✨ Ishga tushirish  
```bash
# Loyihani klon qilish
git clone https://github.com/Bunyodjon-Mamadaliyev/77.uz.git
cd 77.uz

# Vertual muhit yaratish va uni aktiv qilish
python -m venv venv
source venv/bin/activate 
# For Windows: venv\Scripts\activate

# Kerakli kutubxonalarni o'rnatib olish
pip install -r requirements/development.txt

# Muhit o‘zgaruvchilarini sozlash
cp env-example.txt .env # .env faylini oching va kerakli qiymatlarni to‘ldiring

# Pre-commit hooklarini o‘rnatish va sozlash
pre-commit install
pre-commit autoupdate

# Start skriptini bajariladigan qilish
chmod +x start.sh

# Loyihani ishga tushirish
./start.sh

# Modeldagi o‘zgarishlardan migratsiya fayllarini yaratish
python manage.py makemigrations

# Migratsiyalarni ma’lumotlar bazasiga qo‘llash
python manage.py migrate

# Dastur serverini ishga tushirish
python manage.py runserver

```


