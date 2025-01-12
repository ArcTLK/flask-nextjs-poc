from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Root path"

@app.route("/frontend")
def serve_frontend_root():
    # TODO: add authentication check here

    return send_from_directory('public', 'index.html')

@app.route("/frontend/<path:path>")
def serve_frontend_resource_files(path):
    # TODO: add authentication check here
    
    return send_from_directory('public', path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)