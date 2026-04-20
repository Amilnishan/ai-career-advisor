from flask import Flask, render_template, request
from ai_utils import get_advice, get_skills
import markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])     # GET(When a user first visit the page), POST(When a user submits the form)
def home():
    result = ""

    if request.method == "POST":
        name = request.form.get("name")
        goal = request.form.get("goal")
        action = request.form.get("action")

        if action == "advice":
            try:
                raw_result = get_advice(name, goal)
                result = markdown.markdown(raw_result)
            except Exception as e:
                result = "<p style='color: #ff3333; font-weight: bold;'>Something went wrong. Please try again.</p>"
        elif action == "skills":
            try:
                raw_result = get_skills(goal)
                result = markdown.markdown(raw_result)
            except Exception as e:
                result = "<p style='color: #ff3333; font-weight: bold;'>Something went wrong. Please try again.</p>"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)