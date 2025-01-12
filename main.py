from flask import Flask, redirect

app = Flask(__name__, static_folder='public', static_url_path='/frontend')

@app.route("/")
def hello_world():
    return "Root path"

@app.route("/frontend")
def frontend_redirect():
    return redirect("/frontend/index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)