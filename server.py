from flask import Flask, render_template, request,jsonify,redirect,url_for, session
from flask import jsonify, flash, request
app = Flask(__name__)

@app.route("/")
def ini():
    return render_template('Base.html')







if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)