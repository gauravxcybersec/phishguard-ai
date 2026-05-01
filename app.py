from flask import Flask, render_template, request
import joblib
from utils import extract_features, rule_based_check

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    confidence = ""

    if request.method == "POST":
        url = request.form["url"]

        features = [extract_features(url)]

        ml_pred = model.predict(features)[0]
        prob = model.predict_proba(features)[0][ml_pred]

        rule_pred = rule_based_check(url)

        # 🔥 FINAL DECISION
        final_pred = 1 if (ml_pred == 1 or rule_pred == 1) else 0

        if final_pred == 1:
            result = "⚠️ Phishing URL"
        else:
            result = "✅ Safe URL"

        confidence = f"ML Confidence: {round(prob*100,2)}%"

    return render_template("index.html", result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)