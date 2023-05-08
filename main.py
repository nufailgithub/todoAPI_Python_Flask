from flask import Flask,request,Response,jsonify

app = Flask(__name__)

class Item:
    id=""
    title=""
    describe=""

    def __init__(self,id,title,describe):
        self.id =id
        self.title =title
        self.describe =describe

    def toJson(self):
        in_json = {"id":self.id, "title":self.title, "describr":self.describe}
        return in_json

toDoList = []

item1 = Item(id="1", title="Learning Flask", describe="Start learning Flask")
item2 = Item(id="2", title="Learning python", describe="Start learning Python")

toDoList.append(item1.toJson())
toDoList.append(item2.toJson())


@app.route("/todo/list")
def getAllTodos():
    return jsonify(toDoList)

@app.route("/todo", methods=["POST"])
def createNewTodoItem():
    item = Item(**request.get_json())
    toDoList.append(item.toJson())
    return Response('{"message":"success"}', status=201, mimetype='application/json')



if __name__=="__main__":
    app.run(debug=True)