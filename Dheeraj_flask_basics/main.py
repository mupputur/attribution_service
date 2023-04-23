from flask import Flask,jsonify
import mysql.connector
from db_connect import db_connect
app = Flask(__name__)

k={"employees":[
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

obj=db_connect()

@app.route('/helloworld')
def hello_world():
    return jsonify(k)


if __name__ == "__main__":
    app.run(port=80)
