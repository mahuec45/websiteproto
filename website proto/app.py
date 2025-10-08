from flask import Flask, render_template, request, abort

app = Flask(__name__)

# --- Simple in-memory student data (no images) ---
students = [
    {"name": "Taakua Taake", "whanau": "Green",   "initials": "TT", "bio": "Student from Kiribati."},
    {"name": "Louise Treadwell", "whanau": "Yellow", "initials": "LT", "bio": "Prefect and sports leader."},
    {"name": "Leanne Sayers", "whanau": "Red", "initials": "LS", "bio": "Interested in music and art."}
]

# Helper: find student by exact name
def find_student_by_name(name):
    return next((s for s in students if s["name"] == name), None)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Students list with optional search query (use ?q=)
@app.route('/students')
def students_page():
    q = request.args.get('q', '').strip()
    if q:
        results = [s for s in students if q.lower() in s['name'].lower()]
    else:
        results = students
    return render_template('students.html', students=results, query=q)

# Student profile (name used as the URL segment)
@app.route('/profile/<name>')
def profile(name):
    student = find_student_by_name(name)
    if not student:
        return render_template('404.html'), 404
    return render_template('profile.html', student=student)

# Simple whanaus page
@app.route('/whanaus')
def whanaus():
    # For the prototype this is static content rendered from a template
    return render_template('whanaus.html')

if __name__ == '__main__':
    # Run dev server. Visit http://127.0.0.1:5000
    app.run(debug=True)
