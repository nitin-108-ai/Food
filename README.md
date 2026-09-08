# 🍔 Foody - Food Ordering & Delivery System

A full-stack food ordering and delivery web application with a Python Flask REST API, SQLite database, and responsive frontend client including an admin dashboard.

---

## 🚀 Quick Start on Localhost

### Method 1: 1-Click Batch File (Windows)
Simply double-click the **`START_LOCALHOST.bat`** file in the root folder of this project.

---

### Method 2: Manual Setup via Terminal

1. **Navigate to the backend directory:**
   ```bash
   cd Food.Ordering.System5-main/Website2/backend_py
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask server:**
   ```bash
   python app.py
   ```

---

## 🌐 Localhost Access Links

Once the server is running on localhost, open your browser to:

| Portal | Localhost URL |
|---|---|
| 🛍️ **Customer Web App** | [http://localhost:5000/](http://localhost:5000/) |
| 🛡️ **Admin Dashboard** | [http://localhost:5000/admin.html](http://localhost:5000/admin.html) |
| 🔌 **Backend REST API** | [http://localhost:5000/api/v1](http://localhost:5000/api/v1) |

---

## 🔑 Default Login Credentials

### 🛡️ Admin Accounts
- **Main Super Admins:**
  - Email: `nitin@foody.in` | Password: `nitin123`
  - Email: `karan@foody.in` | Password: `karan123`
- **Standard Admin:**
  - Email: `admin@foody.in` | Password: `admin123`

### 👤 Demo User Account
- Email: `demo@foody.in`
- Password: `foody123`

*(You can also register a new user account directly from the frontend)*

---

## 🛠️ Technology Stack

- **Backend:** Python 3.12, Flask, Flask-CORS, PyJWT, Werkzeug
- **Database:** SQLite (`foody.db`)
- **Frontend:** Semantic HTML5, CSS3 (Vanilla), JavaScript (ES6+), FontAwesome Icons
- **Authentication:** JWT (JSON Web Tokens) with hashed passwords

---

## 📁 Project Structure

```
Food/
├── START_LOCALHOST.bat           # 1-Click launcher for localhost server
├── README.md                     # Project documentation & run guide
├── .gitignore                    # Ignored files (caches, temp files)
└── Food.Ordering.System5-main/
    └── Website2/
        ├── START_SERVER.bat      # Local server script inside Website2
        ├── foody-intro.mp4       # Video asset
        ├── backend_py/           # Python Flask backend
        │   ├── app.py            # Main server & REST API routes
        │   ├── models.py         # SQLite database schema & helpers
        │   ├── seed_data.py      # Database seed data
        │   ├── foody.db          # SQLite database file
        │   ├── requirements.txt  # Python package dependencies
        │   └── run.bat           # Backend launcher
        └── frontend/             # Client-side web interface
            ├── index.html        # Customer home & food ordering page
            ├── admin.html        # Admin management portal
            ├── food.html         # Food detail page
            ├── cart.html         # Shopping cart
            ├── checkout.html     # Checkout process
            ├── payment.html      # Payment processing
            ├── orders.html       # Customer order history
            ├── login.html        # Authentication login
            ├── register.html     # User registration
            └── ...               # Additional pages & UI assets
```

---

## 📄 License
This project is for educational and portfolio purposes.