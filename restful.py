from flask import Flask,jsonify,request
app = Flask(__name__)
orders = []
@app.route('/',methods=['GET'])
def test():
    return jsonify({"message":"It works"})
@app.route('/get_all_oders',methods=['GET'])
def get_all_orders():
    return jsonify   ({"orders":orders}) 
@app.route('/get_order/<string:name>', methods=['GET'])
def get_order(name):
    for order in orders:
        if name not in order["name"]:
            return jsonify({"message":"name not found"})
        else:
            langs=[order for order in orders if order["name"]==name]   
            return jsonify({'order':langs[0]})
@app.route('/place_order',methods=['POST'])
def place_order():
    language = {'name':request.json['name']}
    orders.append(language) 
    return jsonify({'languages':orders})

@app.route('/update_order/<string:name>',methods=['PUT'])
def update_order(name):
    langs=[order for order in orders if order['name']==name]    
    langs[0]['name']=request.json['name']
    return jsonify({"order":langs[0]})

@app.route('/remove_item/<string:name>', methods=['DELETE'])
def remove_item(name):  
    langs=[order for order in orders if order['name']==name]
    orders.remove(langs[0])  
    return jsonify({'languages':orders})

    
if __name__ == "__main__":
    app.run(debug=True,port=8000)    