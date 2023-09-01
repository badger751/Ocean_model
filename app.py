# app.py

from flask import Flask, render_template, request, session
from ocean_model import OceanModel  # Corrected import name
import secrets

def generate_secret_key():
    return secrets.token_hex(16)  # Generates a 32-character (16 bytes) hexadecimal secret key


app = Flask(__name__)
# Set the secret key for session management
app.secret_key = generate_secret_key()

ocean_model = OceanModel()  # Create an instance of OceanModel
questions = [
    "On a scale of 1 to 5, how open are you to new experiences and ideas?",
    "How organized and detail-oriented are you in your daily life?",
    "In social situations, how outgoing and talkative are you?",
    "How willing are you to compromise and avoid conflicts in your interactions with others?",
    "How emotionally stable do you consider yourself to be?",
    "How adventurous and thrill-seeking are you in your activities?",
    "How empathetic and compassionate are you towards others' feelings?",
    "How competitive and ambitious are you in achieving your goals?",
    "How patient and relaxed are you in handling stressful situations?",
    "How trusting and cooperative are you when working with others?"
    # Add other questions here...
]
@app.route("/", methods=["GET", "POST"])
def index():
    responses = session.get("responses", [0] * len(questions))
    current_question = session.get("current_question", 0)
    
    if request.method == "POST":
        response = int(request.form.get("response"))
        responses[current_question] = response
        session["responses"] = responses

        if current_question < len(questions) - 1:
            # Display the next question
            current_question += 1
            session["current_question"] = current_question
            return render_template("questions.html", current_question=current_question, current_question_text=questions[current_question])

        # If all questions have been answered, calculate the mean response
        mean_response = sum(responses) / len(responses)
        # Map the mean response to a personality type (you can adjust the thresholds)
        if mean_response <= 2.0:
            personality_type = "N"
        elif mean_response <= 3.0:
            personality_type = "O"
        elif mean_response <= 4.0:
            personality_type = "A"
        else:
            personality_type = "E"
        personality_name = ocean_model.personality_types.get(personality_type, "Unknown")
        return render_template("results.html", personality_type=personality_name)

    # Initialize or reset responses for the first question
    session["responses"] = [0] * len(questions)
    session["current_question"] = 0
    return render_template("questions.html", current_question=current_question, current_question_text=questions[current_question])


if __name__ == "__main__":
    app.run(debug=True)
