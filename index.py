from flask import Flask
from flask import render_template,request
import sqlite3 as sql

global trscount,congresscount,bjpcount
app = Flask(__name__,template_folder='templates')

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('first.html')
@app.route("/votedels")
def secongpg():
    return render_template('second.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
               if request.form.get("congressbutton"):
                 b="congress"
               elif request.form.get('bjpbutton'):
                 b="bjp"
               elif request.form.get('trsbutton'):
                 b='trs'
               print(b)               
               with sql.connect("database.db") as conn:
                  cur = conn.cursor()
              
               t=str(b)
               x=cur.execute("INSERT INTO voteing VALUES (?)",[t] )
               y=cur.execute("select count(*) from voteing where pname='trs'")               
               for i in y:
                    trscount=i
               y=cur.execute("select count(*) from voteing where pname='congress'")               
               for j in y:
                  congresscount=i
               y=cur.execute("select count(*) from voteing where pname='bjp'")               
               for k in y:
                     bjpcount=i

               conn.commit()
               return render_template("third.html")
@app.route('/viewresults',methods=['POST','GET'])
def viewresults():
  with sql.connect("database.db") as conn:
               cur = conn.cursor()
               y=cur.execute("select count(*) from voteing where pname='trs'")               
               for i in y:
                    trscount=i
               y=cur.execute("select count(*) from voteing where pname='congress'")               
               for j in y:
                  congresscount=j
               y=cur.execute("select count(*) from voteing where pname='bjp'")               
               for k in y:
                     bjpcount=k

               conn.commit()
  return render_template("results.html",trscount=trscount,congresscount=congresscount,bjpcount=bjpcount)

# run the application
if __name__ == "__main__":
    app.run(debug=True)