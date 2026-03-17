from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Cloud DevOps Project Running on GCP"

@app.route("/health")
def health():
    return "Application is healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
