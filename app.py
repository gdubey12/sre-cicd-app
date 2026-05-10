from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from SRE Labs", "version": "1.0"})

@app.route('/health')
def health():
    return jsonify({"status": "ok", "version": "1.2"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route("/goodbye")
def goodbye():
    return jsonify({"message": "Goodbye from SRE Labs"})
