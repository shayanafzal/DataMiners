#################################################
# MongoDB and Flask Application
#################################################

# Dependencies and Setup
from flask import Flask, render_template
from flask_pymongo import PyMongo
import code


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# PyMongo Connection Setup
#################################################
app.config["MONGO_URI"] = "mongodb://localhost:27017/snack_brands"
mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################
# Root Route to Query MongoDB & Pass Data Into HTML Template: index.html to Display Data
@app.route("/")
def index():
    snack_brands = mongo.db.snack_brands.find_one()
    return render_template("index.html", snack_brands=snack_brands)

@app.route("/")
def code():
    code = mongo.db.code
    code = code.sales_df()
    code.update({}, code, upsert=True)
    return render_template("index.html", code=code)

# Define Main Behavior
if __name__ == "__main__":
    app.run()