from flask import Flask, render_template, redirect
import scrape_mars
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Establish mongo connection to mars_app db
conn = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(conn)


@app.route("/")
def home():

    mars_data = client.mars_app.mars_info.find_one()

    return render_template("index.html", mars_data=mars_data)


@app.route('/scrape')
def scrape():

    collection = client.mars_app.mars_info
    mars_data = scrape_mars.scrape()

    collection.update({}, mars_data, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

