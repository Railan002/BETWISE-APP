from flask import Flask, jsonify
import prediction  # import your script

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to Betwise Predictions"}

@app.route('/predictions')
def get_predictions():
    return jsonify(prediction.run_predictions())

if __name__ == '__main__':
    app.run()