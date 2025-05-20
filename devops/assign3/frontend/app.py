from flask import Flask, request, render_template
import requests

BACKEND_URL = "http://0.0.0.0:9000"  # Change this to your backend URL
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = dict(request.form)
    response = requests.post(f"{BACKEND_URL}/submit", json=data)
    if response.status_code != 200:
        return response.json()
    return "Data submitted successfully!"

@app.route("/view")
def view():
    data = requests.get(f"{BACKEND_URL}/view").json()
    return data

@app.route("/api")
def api():
    with open("data.txt", "r") as file:
        data = file.read()
    return {"data": data}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)