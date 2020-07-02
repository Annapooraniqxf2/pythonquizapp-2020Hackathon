from quiz_app import db
import datetime
from sqlalchemy import Integer, ForeignKey, String, Column,CheckConstraint,DateTime
from sqlalchemy.sql import table, column

class Questions(db.Model):
    "Table which has Python questions and answers"
    question_id = db.Column(db.Integer,primary_key=True)
    question = db.Column(db.String(50),nullable=False)
    answer = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f"Questions('{self.question_id}', '{self.question}','{self.answer}')"