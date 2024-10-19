from flask import Flask, request,render_template

# data
engineering_branches = [
    "Artificial Intelligence and Data Engineering",
    "Chemical Engineering",
    "Civil Engineering",
    "Computer Science and Engineering",
    "Electrical Engineering",
    "Electronics and Communication Engineering",
    "Mechanical Engineering",
    "Metallurgical and Materials Engineering"
]
course_codes = [
    "CST205", "CST206", "CST207", "CST208", "CST209", "CST210", "CST301", 
]
years = [
    2024,
    2023,
    2022,
    2021,
    2020,
    2019,
    2018,
    2017,
    2016,
    2015,
    2014,
]

app = Flask(__name__, template_folder='templates',static_folder='static')

@app.route('/')
def home():
    return render_template('index.html',engineering_branches=engineering_branches,course_codes=course_codes,years=years)
@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0",port="5000");
