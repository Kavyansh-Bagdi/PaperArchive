from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
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
semester = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'mysql://root:password123@localhost/'
 
mysql = MySQL(app)

app = Flask(__name__, template_folder='templates',static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload',methods = ['get','post'])
def upload():
    return render_template('upload.html',branch = engineering_branches,sem=semester,y=year)

if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0",port="5000");


def addData():
    pass

def readData(something):
    cursor = mysql.connection.cursor()
    queue = 'SELECT DISTINCT ' + something + ' FROM questionpaper;'
    pass