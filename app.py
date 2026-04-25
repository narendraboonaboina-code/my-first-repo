from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Dockerized Python App!"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Important: host='0.0.0.0' so Docker can expose it
    app.run(host="0.0.0.0", port=5000)
