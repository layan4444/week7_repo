from flask import Flask, request, jsonify, render_template

from sqlalchemy import select

 

from database import engine, metadata

from models import courses

 

from db_utils import get_user_skills, get_all_courses

from recommendation import recommend_courses

 

app = Flask(__name__)

metadata.create_all(engine)

# 🔷 Web Page

@app.route("/")

def home():
    return render_template("index.html")

# 🔷 API

@app.route("/api/recommend", methods=["POST"])
def recommend():

    data = request.json
    user_id = data.get("user_id")
    text = data.get("text")

    if user_id:
        skills = get_user_skills(user_id)

    elif text:
        from skill_extraction import extract_skills
        skills = extract_skills(text)

    else:
        return jsonify({"error": "No input provided"}), 400

    courses_data = get_all_courses()

    recommendations = recommend_courses(skills, courses_data)

 
    return jsonify({"recommendations": recommendations})
    

 

 

if __name__ == "__main__":

    app.run(debug=True)