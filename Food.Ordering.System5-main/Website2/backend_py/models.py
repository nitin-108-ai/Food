import sqlite3
import json
import os
import uuid
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from seed_data import RESTAURANTS, FOODS, COUPONS, DEMO_USER, ADMIN_USER, NITIN_ADMIN_USER

DB_FILE = os.path.join(os.path.dirname(__file__), 'foody.db')

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()

    # Users Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            avatar TEXT DEFAULT 'fa-user',
            role TEXT DEFAULT 'user',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    try:
        c.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")
    except Exception:
        pass

    try:
        c.execute("ALTER TABLE users ADD COLUMN is_super_admin INTEGER DEFAULT 0")
    except Exception:
        pass

    # Restaurants Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            cuisine TEXT NOT NULL,
            description TEXT,
            address TEXT,
            phone TEXT,
            image TEXT,
            rating REAL DEFAULT 4.5,
            delivery_time TEXT DEFAULT '25-30 min',
            delivery_fee INTEGER DEFAULT 25,
            is_active INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Foods Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS foods (
            id TEXT PRIMARY KEY,
            restaurant_id TEXT NOT NULL,
            cat TEXT NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            image TEXT,
            price INTEGER NOT NULL,
            discount_price INTEGER,
            food_type TEXT DEFAULT 'VEG',
            rating REAL DEFAULT 4.5,
            preparation_time TEXT DEFAULT '20 min',
            is_available INTEGER DEFAULT 1,
            ingredients TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Addresses Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS addresses (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            type TEXT DEFAULT 'home',
            label TEXT DEFAULT 'Home',
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            line1 TEXT NOT NULL,
            line2 TEXT,
            state TEXT NOT NULL,
            city TEXT NOT NULL,
            pincode TEXT NOT NULL,
            is_default INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Orders Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id TEXT PRIMARY KEY,
            user_id TEXT,
            date TEXT,
            status TEXT DEFAULT 'CONFIRMED',
            subtotal INTEGER DEFAULT 0,
            discount INTEGER DEFAULT 0,
            coupon TEXT,
            delivery_fee INTEGER DEFAULT 0,
            total INTEGER DEFAULT 0,
            payment_method TEXT DEFAULT 'online',
            payment_status TEXT DEFAULT 'PAID',
            address TEXT,
            restaurant_name TEXT DEFAULT 'Foody Kitchen',
            items TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Coupons Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS coupons (
            code TEXT PRIMARY KEY,
            discount_type TEXT DEFAULT 'FLAT',
            discount_value INTEGER NOT NULL,
            min_subtotal INTEGER DEFAULT 0,
            max_discount INTEGER DEFAULT 500,
            is_active INTEGER DEFAULT 1
        )
    ''')

    # Support Tickets Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS support_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            status TEXT DEFAULT 'OPEN',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()

    # Seed Restaurants if empty
    c.execute('SELECT COUNT(*) as count FROM restaurants')
    if c.fetchone()['count'] == 0:
        for r in RESTAURANTS:
            c.execute('''
                INSERT INTO restaurants (id, name, cuisine, description, address, phone, image, rating, delivery_time, delivery_fee, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (r['id'], r['name'], r['cuisine'], r['description'], r['address'], r['phone'], r['image'], r['rating'], r['delivery_time'], r['delivery_fee'], r['is_active']))

    # Seed Foods if empty
    c.execute('SELECT COUNT(*) as count FROM foods')
    if c.fetchone()['count'] == 0:
        for f in FOODS:
            c.execute('''
                INSERT INTO foods (id, restaurant_id, cat, name, description, image, price, discount_price, food_type, rating, preparation_time, is_available, ingredients)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (f['id'], f['restaurant_id'], f['cat'], f['name'], f['description'], f['image'], f['price'], f['discount_price'], f['food_type'], f['rating'], f['preparation_time'], f['is_available'], json.dumps(f['ingredients'])))

    # Seed Coupons if empty
    c.execute('SELECT COUNT(*) as count FROM coupons')
    if c.fetchone()['count'] == 0:
        for co in COUPONS:
            c.execute('''
                INSERT INTO coupons (code, discount_type, discount_value, min_subtotal, max_discount, is_active)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (co['code'], co['discount_type'], co['discount_value'], co['min_subtotal'], co['max_discount'], co['is_active']))

    # Seed Demo User if not exists
    c.execute('SELECT id FROM users WHERE email = ?', (DEMO_USER['email'],))
    if not c.fetchone():
        hashed = generate_password_hash(DEMO_USER['password'])
        c.execute('''
            INSERT INTO users (id, name, email, phone, password, avatar, role)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (DEMO_USER['id'], DEMO_USER['name'], DEMO_USER['email'], DEMO_USER['phone'], hashed, DEMO_USER['avatar'], 'user'))

    # Seed Admin User if not exists
    c.execute('SELECT id FROM users WHERE email = ?', (ADMIN_USER['email'],))
    hashed_admin = generate_password_hash(ADMIN_USER['password'])
    if not c.fetchone():
        c.execute('''
            INSERT INTO users (id, name, email, phone, password, avatar, role, is_super_admin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (ADMIN_USER['id'], ADMIN_USER['name'], ADMIN_USER['email'], ADMIN_USER['phone'], hashed_admin, ADMIN_USER['avatar'], 'admin', 1))
    else:
        # Ensure role is admin and is_super_admin = 1
        c.execute("UPDATE users SET name = ?, role = 'admin', is_super_admin = 1, password = ? WHERE email = ?", (ADMIN_USER['name'], hashed_admin, ADMIN_USER['email']))

    # Seed Main Admin User (Nitin) if not exists
    c.execute('SELECT id FROM users WHERE email = ?', (NITIN_ADMIN_USER['email'],))
    hashed_nitin = generate_password_hash(NITIN_ADMIN_USER['password'])
    if not c.fetchone():
        c.execute('''
            INSERT INTO users (id, name, email, phone, password, avatar, role, is_super_admin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (NITIN_ADMIN_USER['id'], NITIN_ADMIN_USER['name'], NITIN_ADMIN_USER['email'], NITIN_ADMIN_USER['phone'], hashed_nitin, NITIN_ADMIN_USER['avatar'], 'admin', 1))
    else:
        # Ensure role is admin and is_super_admin = 1
        c.execute("UPDATE users SET name = ?, role = 'admin', is_super_admin = 1, password = ? WHERE email = ?", (NITIN_ADMIN_USER['name'], hashed_nitin, NITIN_ADMIN_USER['email']))

    conn.commit()
    conn.close()
    print("[OK] SQLite Database initialized and seeded successfully!")

# Initialize DB on module load
init_db()
