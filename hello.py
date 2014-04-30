import os
from flask import Flask, render_template, request, redirect, url_for

from textblob import TextBlob
from twython import Twython
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__,template_folder=tmpl_dir)
app.debug = False

@app.route('/', methods = ['POST'])
def index():
	try:
		APP_KEY = "KEY";
		APP_SECRET = "SECRET";

		twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
		ACCESS_TOKEN = twitter.obtain_access_token()
		text = request.form['text']

		twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

		
		search = twitter.cursor(twitter.search,q=text,count=1000)
		
			
		totalSent = 0
		i = 0 
		for result in search:
			if i > 500:
				break;
			totalSent += TextBlob(result['text']).sentiment.polarity
			i += 1

		return render_template('index.html',name = "the twitter gods rated " + text, finding = str(wordOfIt(round(totalSent/i,2))),errorThing = None)
	except:	
		return render_template('index.html',name = None, finding = None, errorThing =  "There was an error with your input. Please try something else!")
@app.route('/')
def thing():
	return render_template('index.html',finding = None,errorThing = None,name = None)

@app.route('/about')
def about():
	return render_template("about.html")

def wordOfIt(total):
	return  str(((total+1)*5)) + "/10"