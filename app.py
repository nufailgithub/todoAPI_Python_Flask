from flask import Flask,jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy    #To SQLlite DB
import os       #to set tha path for DB file
import jwt      #to create json web token
import datetime  #to set exp in generate web token

app = Flask(__name__)

app.config['SECRET_KEY'] = "thisIsSecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(app.root_path,'todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)


#CREATE DATABASE AND TABLE
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)

@app.route('/todos', methods=['POST'])
def login():
    auth = request.authorization

    if auth.password == 'password':
        token = jwt.encode({'id':user.id, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
        data = request.get_json()

        new_task = Task(id=data['id'], title=data['title'], complete=False)

        db.session.add(new_task)
        db.session.commit()

        return make_response(jsonify("New task is created!"), 200)

    else:
        return make_response('Could not verify!', 401, {"WWW-Authenticate": 'Basic realm="Login Required'})


"""
@app.route('/login', methods=['POST'])
def login():
    username = request.authorization.username
    password = request.authorization.password

    if password == 'password':
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return make_response(jsonify({'token': token.decode('UTF-8')}), 200)
    else:
        return make_response(jsonify({'message': 'Could not verify!'}), 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})


@app.route('/todos', methods=['POST'])
def create_todo():
    token = request.headers.get('Authorization')
    if not token:
        return make_response(jsonify({'message': 'Missing token'}), 401)

    try:
        token = token.split(' ')[1]
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        if 'username' not in data:
            return make_response(jsonify({'message': 'Invalid token'}), 401)
    except:
        return make_response(jsonify({'message': 'Invalid token'}), 401)

    if not request.json or not 'title' in request.json:
        return make_response(jsonify({'message': 'Missing title'}), 400)

    new_todo = Todo(title=request.json['title'], complete=False)
    db.session.add(new_todo)
    db.session.commit()

    return make_response(jsonify({'message': 'New todo created!'}), 201)


"""
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    result = []
    for todo in todos:
        result.append({
            'id': todo.id,
            'title': todo.title,
            'complete': todo.complete,
        })
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)