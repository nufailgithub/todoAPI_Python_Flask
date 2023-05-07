from flask import Flask, jsonify, request
import sqlite3
from flask_marshmallow import Marshmallow
import os  # for access SQL lite

app = Flask(__name__)

"""
@app.route('/', methods=['GET'])
def home():
    return jsonify({'msg': 'Welcome To our site'})
"""

"""SETTING THE DB """

base_directory = os.path.abspath(os.path.dirname(__file__))     #GETTING THE PATH
#Print(base_directory)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(base_directory,'DB.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = sqlite3.connect(DB)
cursor = db.cursor()
marsh = Marshmallow(app)


class Task(DB.Model):
    num = DB.Column(DB.Integer, autoincrement=True )
    task=DB.Column(DB.String, primary_key=True)
    status=DB.Column(DB.String(100))

    def __init__(self,task,status):
        self.task = task
        self.status = status

class TaskSchema(marsh.Schema):
    class Meta:
        fields = ('num', 'task', 'status')

task_schema = TaskSchema()
task_schema = TaskSchema(many=True)


if __name__ == '__main__':
    app.run(debug=True)
