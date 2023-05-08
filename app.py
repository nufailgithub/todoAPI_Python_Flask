from flask import Flask, render_template,jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

#CREATE MODEL
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)


@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'secret':
        return
    return make_response('Could not verify!', 401,{'WWW-Authenticate' :'Basic realm="Login Required'})


@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()

    new_task = Task(name=data['name'], content=data['content'], complete=False)

    db.session.add(new_task)
    db.session.commit()

    return make_response(jsonify("New task is created!"), 200)


@app.route('/about')
def about():
    return '<h1>About page</h1>'

if __name__ == "__main__":
    app.run(debug=True)