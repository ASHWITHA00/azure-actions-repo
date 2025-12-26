from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from Azure!</h1><p>My Python Web App is running.</p>"

if __name__ == "__main__":
    app.run()
