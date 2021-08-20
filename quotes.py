from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:Stacyw12!@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://nwtetustodprol:ef515748c0ad4f9e00253d2e7f76baa8892691500b20e3fbb3cf0fbcab89a93b@ec2-35-153-114-74.compute-1.amazonaws.com:5432/df77r7dgcaibvq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

#This created the table in PostGres database
class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))




   	  #else:
		 #return render_template('quotes.html')
