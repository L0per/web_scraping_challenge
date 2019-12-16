from flask import Flask, render_template, redirect
import scrape_mars
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Establish mongo connection to mars_app db
conn = 'mongodb://localhost:27017/mars_app'
client = pymongo.MongoClient(conn)


@app.route("/")
def home():

    return render_template("index.html")


@app.route('/scrape')
def scrape():

    collection = client.db.mars_info
    mars_data = scrape_mars.scrape()

    collection.update({}, mars_data, upsert=True)

    return redirect("/")

