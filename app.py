from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity)
from dotenv import load_dotenv
from openai import OpenAI
import os
import pandas as pd
import sqlite3

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in .env")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure app
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "super-secret-key")
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

with app.app_context():
    db.create_all()

# Signup endpoint
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"msg": "Email and password required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed_pw = generate_password_hash(password)
    new_user = User(email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

# Protected profile route
@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(email=current_user), 200

# Another protected route example
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Profitability check endpoint
@app.route('/api/check_profitability', methods=['POST'])
def check_profitability():
    try:
        data = request.get_json()
        result = data.get("result")
        total_trade = result.get("totalCosts")
        total_retail = result.get("totalRevenue")
        profit_margin = (result.get("profit") / total_retail) * 100 if total_retail else 0

        prompt = (
            f"Total Trade Cost: £{total_trade:.2f}\n"
            f"Total Retail Revenue: £{total_retail:.2f}\n"
            f"Profit Margin: {profit_margin:.2f}%\n"
            "Give 3 quick suggestions to improve profitability, keep them actionable."
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a profitability expert."},
                {"role": "user", "content": prompt}
            ]
        )

        ai_suggestions = response.choices[0].message.content

        return jsonify({
            "ai_suggestions": ai_suggestions
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run app
if __name__ == "__main__":
    app.run(debug=True)
