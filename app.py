from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify(message="Olá Mundo!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='')
