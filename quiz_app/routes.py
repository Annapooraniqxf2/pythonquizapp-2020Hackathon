from flask import render_template, url_for, flash, redirect, jsonify, request, Response, session
from quiz_app import app
from quiz_app import db
import random,datetime
from quiz_app.models import Questions
from apscheduler.schedulers.background import BackgroundScheduler


@app.route("/index")
def index():
    "The index page"
    return render_template("index.html")


def fetch_question_from_db():
    "Fetch the questions from the db"
    #Fetch from the database
    python_all_questions = Questions.query.all()
    total_no_of_questions = len(python_all_questions)
    #python_all_questions = random.shuffle(python_all_questions)
    for each_question in random.sample(python_all_questions,total_no_of_questions):
        question = each_question.question
        question_id = each_question.question_id
        data = {"question_id":question_id, 'question':question}

    return data


def fetch_answer_from_db(question_id):
    "Fetch the answers from db"
    fetch_answer_for_quest_id = Questions.query.filter(Questions.question_id == question_id).value(Questions.answer)
    data ={"answer":fetch_answer_for_quest_id}

    return data


@app.route("/startquiz",methods=["GET","POST"])
def start_quiz():
    "Start the quiz"
    if request.method == 'GET':
        return render_template("startquiz.html")
    if request.method == 'POST':
        app_question = fetch_question_from_db()
        return jsonify(app_question)


@app.route("/answer",methods=["GET","POST"])
def show_answer():
    "Fetch the answer"
    if request.method == "POST":
        question_id = request.form.get("questionid")
        app_answer = fetch_answer_from_db(question_id)

    return jsonify(app_answer)


@app.route("/campaignquestion",methods=["GET","POST"])
def show_question_of_the_day():
    "It fetches one question from the database"
    if request.method == 'POST':
        question_id = request.form.get("questionid")
        answer = fetch_answer_from_db(question_id)

        return jsonify(answer)

    my_question = fetch_question_from_db()

    return render_template("campaignquestion.html", result=jsonify(my_question))


def scheduler_job():
    "Runs this job in the background"
    with app.test_request_context('/campaignquestion', method=['GET','POST']):
        #ctx= app.test_request_context('/campaignquestion', method=['GET','POST'])
        #ctx.push()
        show_question_of_the_day()


#Running the task in the background to update the jobcandidate table
sched = BackgroundScheduler(daemon=True)
#sched.add_job(scheduler_job,'cron', minute='*')
sched.add_job(scheduler_job,'cron',day_of_week='mon-fri', hour='*', minute='*')
sched.start()