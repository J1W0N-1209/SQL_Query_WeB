from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/query/',methods=["GET","POST"])
def query():
  if request.method == "POST":
    query = request.form["query"]
    with sqlite3.connect("database.db") as con:
      cur = con.cursor()
      try: 
        cur.execute(f"{query}")
      except:
        return render_template('index.html',error="Error")
      rows = cur.fetchall()
    print(rows)
  return render_template('index.html',rows=rows)
if __name__ == '__main__':
  app.run(debug=True)