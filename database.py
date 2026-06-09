import sqlite3
import config

def get_connection():
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY, username TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    c.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE, name TEXT NOT NULL,
        phone TEXT NOT NULL, age TEXT NOT NULL,
        course TEXT NOT NULL, status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id))""")
    c.execute("""CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL, price INTEGER DEFAULT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    c.execute("""CREATE TABLE IF NOT EXISTS schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course TEXT NOT NULL, teacher TEXT NOT NULL,
        level TEXT NOT NULL, days TEXT NOT NULL,
        time TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    default_courses = ["Matematika", "Ingliz tili", "Informatika", "Fizika"]
    for course in default_courses:
        c.execute("INSERT OR IGNORE INTO courses (name) VALUES (?)", (course,))
    conn.commit()
    conn.close()
    print("Ma'lumotlar bazasi tayyor.")

def add_user_if_not_exists(user_id, username):
    conn = get_connection()
    conn.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit(); conn.close()

def is_already_registered(user_id):
    conn = get_connection()
    row = conn.execute("SELECT id FROM students WHERE user_id = ?", (user_id,)).fetchone()
    conn.close(); return row is not None

def get_student_status(user_id):
    conn = get_connection()
    row = conn.execute("SELECT status FROM students WHERE user_id = ?", (user_id,)).fetchone()
    conn.close(); return row["status"] if row else None

def save_student(user_id, name, phone, age, course):
    conn = get_connection()
    conn.execute("INSERT OR REPLACE INTO students (user_id, name, phone, age, course, status) VALUES (?, ?, ?, ?, ?, 'pending')",
                 (user_id, name, phone, age, course))
    conn.commit(); conn.close()

def get_student(user_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM students WHERE user_id = ?", (user_id,)).fetchone()
    conn.close(); return dict(row) if row else None

def update_student_status(user_id, status):
    conn = get_connection()
    conn.execute("UPDATE students SET status = ? WHERE user_id = ?", (status, user_id))
    conn.commit(); conn.close()

def get_pending_students():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM students WHERE status = 'pending' ORDER BY created_at DESC").fetchall()
    conn.close(); return [dict(r) for r in rows]

def get_approved_students():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM students WHERE status = 'approved' ORDER BY created_at DESC").fetchall()
    conn.close(); return [dict(r) for r in rows]

def get_all_students():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM students ORDER BY created_at DESC").fetchall()
    conn.close(); return [dict(r) for r in rows]

def get_all_user_ids():
    conn = get_connection()
    rows = conn.execute("SELECT user_id FROM users").fetchall()
    conn.close(); return [r["user_id"] for r in rows]

def get_all_courses():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM courses ORDER BY name").fetchall()
    conn.close(); return [dict(r) for r in rows]

def get_courses_with_price():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM courses ORDER BY name").fetchall()
    conn.close(); return [dict(r) for r in rows]

def get_course_by_id(course_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM courses WHERE id = ?", (course_id,)).fetchone()
    conn.close(); return dict(row) if row else None

def add_course(name):
    conn = get_connection()
    conn.execute("INSERT OR IGNORE INTO courses (name) VALUES (?)", (name,))
    conn.commit(); conn.close()

def set_course_price(course_id, price):
    conn = get_connection()
    conn.execute("UPDATE courses SET price = ? WHERE id = ?", (price, course_id))
    conn.commit(); conn.close()

def delete_course(course_id):
    conn = get_connection()
    conn.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit(); conn.close()

def get_all_schedules():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM schedules ORDER BY course, time").fetchall()
    conn.close(); return [dict(r) for r in rows]

def add_schedule(course, teacher, level, days, time):
    conn = get_connection()
    conn.execute("INSERT INTO schedules (course, teacher, level, days, time) VALUES (?, ?, ?, ?, ?)",
                 (course, teacher, level, days, time))
    conn.commit(); conn.close()

def delete_schedule(schedule_id):
    conn = get_connection()
    conn.execute("DELETE FROM schedules WHERE id = ?", (schedule_id,))
    conn.commit(); conn.close()
