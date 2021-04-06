from flask import *
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "ThisIsASecretKey"
debug = DebugToolbarExtension(app)

curr_question = 0
questions = satisfaction_survey.questions

@app.route('/')
def get_home():
    session['RESPONSES'] = []
    return render_template('home.html', curr_question=curr_question)

@app.route(f'/questions/<int:question>')
def get_question(question):
    """Gets and displays the questions"""
    if question == curr_question and question < len(questions):
        question_text = questions[question].question
        choices = questions[question].choices
        return render_template(f'questions.html', question_text=question_text, choices=choices, question=question)
    elif curr_question >= len(questions):
        flash('You Have Completed The Survey!')
        return redirect('/thanks')
    else:
        flash("Trying to access an invalid question! Redirected to current question!")
        return redirect(f'/questions/{curr_question}')

@app.route('/answer', methods=["POST"]) 
def get_answer():
    """Adds the answer to the RESPONSES list and increments the current question"""
    RESPONSES = session['RESPONSES']
    global curr_question
    if curr_question <= len(questions):
        curr_question += 1
    choice = request.args['choice']
    RESPONSES.append(choice)
    session["RESPONSES"] = RESPONSES
    return redirect(f'/questions/{curr_question}')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')