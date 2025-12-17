from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

#loading the saved model
model = pickle.load(open("spam_model.pkl", "rb"))
vector = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.form['message']

    msg_vector = vector.transform([msg])
    prediction = model.predict(msg_vector)[0]

    return render_template(
        'index.html',
        result=f'This email is: {prediction.upper()}'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
