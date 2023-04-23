import mysql.connector


class db_connect():
    def __init__(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="1234", database="flaskdb")
            cur=con.cursor(dictionary=True)
            cur.execute("Select * from emp")
            result=cur.fetchall()
            print(result)
            print("Successful")

        except:
            print("Some error occured")
