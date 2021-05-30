from flask import Flask, jsonify, request
app = Flask(__name__)

tasks=[
    {
        "Contact":"9987644456",
        "Name":"Raju",
        "done":False,
        "id":1
    },
    {
        "Contact":"9876543222",
        "Name":"Rahul",
        "done":False,
        "id":2
    }
]


@app.route('/add-data',methods=["POST"])
def add_task():
    if(not request.json):
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        })

    task={
        "Contact":request.json.get("Contact"),
        "Name":request.json["Name"],
        "done":False,
        "id":tasks[-1]["id"]+1
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfuly"

    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)