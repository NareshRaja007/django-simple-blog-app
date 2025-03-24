(Simple Blog Post Application - Django + PostgreSQL)

# 📝 Simple Blog Post Application (Django + PostgreSQL)

This is a **minimal blog post application** built using **Django** and **PostgreSQL**.  
It allows users to **create and view blog posts**.

---

## 📌 Features
- 📝 **Create Blog Posts**  
- 📖 **View List of Blog Posts**  
- ✅ **Form Validation** (Title & Content required)  
- 🗄️ **PostgreSQL Database**  
- 🔍 **Unit Tests** for model and views  

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/simple_blog.git
cd simple_blog
2️⃣ Backend Setup (Django + PostgreSQL)
🔹 Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
🔹 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 Configure PostgreSQL
Update DATABASES in settings.py with your PostgreSQL credentials.

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
🔹 Run Migrations
bash
Copy
Edit
python manage.py migrate
🔹 Create Superuser (Optional)
bash
Copy
Edit
python manage.py createsuperuser
🔹 Start Server
bash
Copy
Edit
python manage.py runserver
Server will be available at http://127.0.0.1:8000/

3️⃣ Usage
🔹 View Blog Posts
Visit: http://127.0.0.1:8000/posts/

🔹 Create a Blog Post
Visit: http://127.0.0.1:8000/posts/create/

4️⃣ Running Unit Tests
To verify model and view functionality, run:

bash
Copy
Edit
python manage.py test
