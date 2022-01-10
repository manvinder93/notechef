from flask import Flask,render_template,request,url_for
import sqlite3
app = Flask(__name__)
 

conn=sqlite3.connect('login.db',check_same_thread=False)

def add_user(user,passwd,usr_id):
    conn.execute('INSERT INTO login(user_id,username,password) values(?,?,?)',(usr_id,user,passwd,))
    conn.commit()

    return

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods = ['POST'])
def login():
    global count_users
    
    user = request.form['username']
    passwd = request.form['password']
    cursor=conn.execute('SELECT * FROM login WHERE username = ? and password= ?',(user,passwd,))
    if len(cursor.fetchall())==0 and count_users==0:
        add_user(user,passwd,count_users)
        count_users+=1

    elif len(cursor.fetchall())==0 and count_users>0:
        count_users+=1
        add_user(user,passwd,count_users)
    

    return render_template('home.html',name=user)
    


if __name__ == '__main__':
   app.run(debug=True)