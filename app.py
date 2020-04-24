from flask import Flask,render_template,request, url_for ,redirect
from flask_mysqldb import MySQL
from flask_mail import Mail
from main_final import prachi
import schedule
import time

app = Flask(__name__)

app.config['SECRET_KEY']='123456789'
app.config['MYSQL_HOST'] = 'localhost'    
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= 'your sql password'
app.config['MYSQL_DB']='data'


mysql=MySQL(app)








@app.route('/',methods=['GET','POST'])
@app.route('/index')
def index():
	


	return render_template("index.html")
	   
@app.route('/about')
def about():
	


	return render_template("about.html")

@app.route('/contact')
def contact():
	


	return render_template("contact.html")


@app.route("/register", methods=['GET','POST'])
def register():
	
	if request.method=='POST':
		userdetails=request.form
		fname=userdetails['fname']
		lname=userdetails['lname']
		email=userdetails['email']
		phone_no=userdetails['phone_no']
		name=fname+" "+lname
		cur=mysql.connection.cursor()
		cur.execute("insert into credentials values(%s,%s,%s)",(name,email,phone_no))
		mysql.connection.commit()
		cur.close()
		return redirect(url_for('index'))

	return render_template('register.html')



@app.route("/pickup",methods=['GET','POST'])
def pickup():

	if request.method=='POST':

		userdetails=request.form
		mail=userdetails['pmail']
		drop=userdetails['drop']
		time=userdetails['ptime']
		date=userdetails['pdate']
		cur=mysql.connection.cursor()
		cur.execute("insert into pickup values(%s,%s,%s,%s);",(drop,date,time,mail))
		mysql.connection.commit()
		cur.close()		
		
         
	return render_template('pickup.html')     


@app.route("/dropoff",methods=['GET','POST'])
def dropoff():
	if request.method=='POST':

		userdetails=request.form
		mail=userdetails['dmail']
		pick=userdetails['pick']
		time=userdetails['dtime']
		date=userdetails['ddate']
		cur=mysql.connection.cursor()
		cur.execute("insert into dropoff values(%s,%s,%s,%s)",(pick,date,time,mail))
		mysql.connection.commit()
		cur.close()
		
	return render_template('dropoff.html')    


@app.route("/start")
def hello():

	
	prachi()
	
	# schedule.every().hour.do(prachi)
	
	# while True:
	#     schedule.run_pending()
	#     time.sleep(1)
		

	return "done"



if __name__ == '__main__':    
	app.run(debug=True)
