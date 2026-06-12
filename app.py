from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("lr_scaler.pkl", "rb") as f:
    model = pickle.load(f)


# ✅ HOME ROUTE (THIS FIXES 404)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[
        data["area"],
        data["bedrooms"],
        data["bathrooms"],
        data["floors"],
        data["age"],
        data["distance"],
        data["garage"],
        data["parking"],
        data["garden"],
        data["security"],
        data["school_nearby"],
        data["hospital_nearby"],
        data["shopping_mall_nearby"],
        data["public_transport"],
        data["crime_rate"],
        data["population_density"],
        encode_location(data["location"])["location_medium"],
        encode_location(data["location"])["location_premium"],
        encode_income(data["income_level"])["income_level_low"],
        encode_income(data["income_level"])["income_level_mid"]
    ]])


    price = model.predict(features)[0]
    return jsonify({"price": round(float(price), 2)})

def encode_location(location):
    return {
        "location_medium": 1 if location == "medium" else 0,
        "location_premium": 1 if location == "premium" else 0
    }

def encode_income(income):
    return {
        "income_level_low": 1 if income == "low" else 0,
        "income_level_mid": 1 if income == "mid" else 0
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)