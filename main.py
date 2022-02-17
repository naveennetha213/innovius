import json

#import content as content
from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import hashlib

app = Flask(__name__)

app.secret_key = 'aaa'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'naveen213'
app.config['MYSQL_DB'] = 'innovius'

mysql = MySQLdb(app)


@app.route('/reg', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        emp_id = request.json['emp_id']
        name = request.json['name']
        mobilenumber = request.json['mobilenumber']
        age = request.json['age']
        address = request.json['address']
        mail_id = request.json['mail_id']
        password = request.json['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('insert into user_signup values(null,%s,%s,%s,%s,%s,%s)', (
            emp_id, name, mobilenumber, age, address, mail_id, password))
        mysql.connection.commit()
        return 'Registration successful'
    else:
        return " registration was un successful"
