from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('survey_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS responses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name TEXT,
                        phone TEXT,
                        email TEXT,
                        location TEXT,
                        family_members INTEGER,
                        employer TEXT,
                        nationality TEXT,
                        net_income REAL,
                        housing_support TEXT,
                        current_housing_status TEXT,
                        monthly_rent REAL
                    )''')
    conn.commit()
    conn.close()

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    conn = sqlite3.connect('survey_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO responses (full_name, phone, email, location, family_members, employer, nationality, net_income, housing_support, current_housing_status, monthly_rent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (data['full_name'], data['phone'], data['email'], data['location'], data.get('family_members', 0), data['employer'], data['nationality'], data.get('net_income', 0), data['housing_support'], data['current_housing_status'], data.get('monthly_rent', 0)))
    conn.commit()
    conn.close()
    return "شكراً لتقديم الاستقصاء!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render يستخدم متغير البيئة PORT
    app.run(host='0.0.0.0', port=port)        # تشغيل التطبيق على 0.0.0.0

