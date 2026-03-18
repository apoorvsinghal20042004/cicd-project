from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    # We are changing the version to 1.0.1, but our test still expects 1.0.0
    return jsonify({"status": "healthy", "version": "1.0.1"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
