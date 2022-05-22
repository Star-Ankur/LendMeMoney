from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'M@nym5d5'
app.config['MYSQL_DB'] = 'users'
 
mysql = MySQL(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('homet.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST' :
        #fetch form data
        fusername = request.form['username']
        femail = request.form['email']
        fpassword = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO details(username,email,password) VALUES(%s,%s,%s)',(fusername,femail,fpassword))
        mysql.connection.commit()
        cur.close()
        return 'success'
    else:
        return render_template('Signup.html')

@app.route('/signin' , methods=['GET', 'POST'])
def signin():
    error='*Either the username or the password do not match!'
    if request.method == 'POST' :
        fusername= request.form['username']
        fpassword = request.form['password']
        cur = mysql.connection.cursor()
        res = cur.execute("SELECT id FROM details WHERE username = (%s) AND password = (%s)",(fusername,fpassword))
        if res > 0:
            return 'success'
        else:
            return render_template('Signin.html',error = error )
    else :
        return render_template('Signin.html')


    
if __name__=='__main__':
    app.run(debug=True)


