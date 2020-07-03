import db
import flask
from flask import jsonify, request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route("/", methods=['GET'])
def home():
	return db.get_all()

@app.route("/increase/<name>/<stat>", methods=['GET'])
def increase(name, stat):
	db.increase_count(name, stat)
	return jsonify("increased %s by 1 for %s" % (stat, name))

@app.route("/decrease/<name>/<stat>", methods=['GET'])
def decrease(name, stat):
	db.decrease_count(name, stat)
	return jsonify("decreased %s by 1 for %s" % (stat, name))

app.run(host='0.0.0.0')
