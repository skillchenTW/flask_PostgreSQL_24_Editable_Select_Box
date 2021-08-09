from flask import Flask, render_template, request, jsonify
import psycopg2
import psycopg2.extras
 
app = Flask(__name__)
 
app.secret_key = "skillchen-secret_key"
 
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "dba"
     
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) 

@app.route('/')
def index():    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select * from countries Order by name ASC")
    countrylist = cur.fetchall()
    return render_template('index.html',countrylist=countrylist)
 
@app.route("/insert",methods=["POST","GET"])
def insert():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == "POST":
        fullname = request.form["name"]
        country = request.form["country"]
        cur.execute("insert into tbl_user(fullname,country) values(%s,%s)",[fullname,country])
        conn.commit()
        cur.close()    
    return jsonify('New Records added successfully')

if __name__ == "__main__":
    app.run(debug=True)