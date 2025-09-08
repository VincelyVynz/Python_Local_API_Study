from flask import Flask, jsonify



app = Flask(__name__)

@app.route('/')
def return_json():
    return jsonify({
  "message": "hello world"
})

@app.route('/expenses')
def return_expenses():
    return jsonify({
        "fruits" : {
            "apples" : 10,
            "oranges" : 20,
            "pears" : 30,
            "bananas" : 40,
            "grapes" : 50
        },
        "bills": {
            "phone bill" : 500,
            "electric bill" : 1080,
            "water bill" : 1000
        }
    })







if __name__ == '__main__':
    app.run()
