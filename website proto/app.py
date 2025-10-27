from flask import Flask, render_template, request, abort

app = Flask(__name__)

# --- Simple in-memory student data (no images) ---
students = [
    {"name": "Taakua Taake", "whanau": "Green whanau", "initials": "TT", "bio": "From Kiribati.", "info": "Kiribati", "pronunciation": "Tah-ah-koo-ah Tah-keh"},
    {"name": "Atauea Airam", "whanau": "Yellow whanau", "initials": "AA", "bio": "From Samoa.","info": "Samoan", "pronunciation": "Ah-tah-oo-where Eye-rahm"},
    {"name": "Tebiri Teun", "whanau": "Red whanau", "initials": "TT", "bio": "From Kiribati.", "info": "Kiribati", "pronunciation": "Teh-bih-ree Teh-oo-un"},
    {"name": "Tiua Kanipule-Eritai", "whanau": "Blue whanau", "initials": "TK", "bio": "From Tonga.", "info": "Tongan", "pronunciation": "Tee-wah Kah-neh-pulley Eh-rih-shy"},
    {"name": "Tulua Hurbert", "whanau": "Purple whanau", "initials": "TH", "bio": "From Tuvalu.", "info": "Tuvaluan", "pronunciation": "Too-loo-ah Her-bert"},
    {"name": "Namakei Obaria", "whanau": "Green whanau", "initials": "NO", "bio": "From Kiribati.", "info": "Kiribati", "pronunciation": "Nah-mah-kay Oh-bah-ree-ah"},
    {"name": "Tipasa Manumalo", "whanau": "Purple whanau", "initials": "TM", "bio": "From Samoa.", "info": "Samoan", "pronunciation": "Tee-pah-sah Mah-noo-mah-lo"},
    {"name": "Uebena Uereti", "whanau": "Purple whanau", "initials": "UU", "bio": "From Tuvalu.", "info": "Tuvaluan", "pronunciation": "Weh-beh-nah Weh-reh-tee"},
    {"name": "Neemia Arobati", "whanau": "Red whanau", "initials": "NA", "bio": "From Kiribati.", "info": "Kiribati", "pronunciation": "Knee-mee-ah Ah-row-bah-tee"},
    {"name": "Teburoro Burenatu", "whanau": "Yellow whanau", "initials": "TB", "bio": "From Kiribati.", "info": "Kiribati", "pronunciation": "Teh-boh-roh-roh Boo-reh-nah-too"},
    {"name": "Sani Rambande Dewage", "whanau": "Blue whanau", "initials": "SD", "bio": "From Fiji.", "info": "Fijian", "pronunciation": "Sunny Rahm-bahn-deh Dew-age"},
    {"name": "Joseph Rambande Dewage", "whanau": "Blue whanau", "initials": "JD", "bio": "From Fiji.", "info": "Fijian", "pronunciation": "Joseph Rahm-bahn-deh Dew-age"},
    {"name": "Tahere Hemana-Walker", "whanau": "Red whanau", "initials": "TH", "bio": "From New Zealand.", "info": "Māori", "pronunciation": "Tah-heh-reh He-mah-nah Walker"},
    {"name": "Makaiah Davis", "whanau": "Yellow whanau", "initials": "MD", "bio": "From New Zealand.", "info": "Māori", "pronunciation": "Mah-kai-ah Davis"},
    {"name": "Waikeringa Karaitiana", "whanau": "Green whanau", "initials": "WK", "bio": "From New Zealand.", "info": "Māori", "pronunciation": "Why-keh-ring-ah Kah-rye-tee-ahn-ah"},
    {"name": "Teraoi Vaitemwa", "whanau": "Purple whanau", "initials": "TV", "bio": "From Tuvalu.", "info": "Tuvaluan", "pronunciation": "Teh-roy vai-teh-mwah"},
    {"name": "Eneriata Kotua", "whanau": "Green whanau", "initials": "EK", "bio": "From Tuvalu.", "info": "Tuvaluan", "pronunciation": "Eh-ner-ree-ah-tah Koh-too-ah"},
    {"name": "Hamon Robert", "whanau": "Red whanau", "initials": "HR", "bio": "From Kiribati.", "info": "Kiribati", "pronunciation": "Ah-mon Robert"},
    {"name": "Riciaban Ah Lee", "whanau": "Yellow whanau", "initials": "RA", "bio": "From Fiji.", "info": "Fijian", "pronunciation": "Wri-sea-ah-bahn Ah Lee"},
    {"name": "Tatibene Abere", "whanau": "Blue whanau", "initials": "TA", "bio": "From Kiribati.", "info": "Kiribati", "pronunciation": "Tah-see-ben-eh Ah-beh-reh"},
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
    sorted_students = sorted(students, key=lambda x: x['name'])
    return render_template('students.html', students=sorted_students)
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

@app.route('/whanaus')
def whanaus():
    # For the prototype this is static content rendered from a template
    return render_template('whanaus.html')

if __name__ == '__main__':
    # Run dev server. Visit http://127.0.0.1:5000
    app.run(debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
