from flask import Flask
from flask_cors import CORS

from wallet import Wallet

app = Flask(__name__)
wallet = Wallet()
CORS(app)


@app.route('/', methods=['GET'])
def get_ui():
    return 'This works!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
