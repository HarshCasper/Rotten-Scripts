
from flask import Flask,render_template,request,g ,session
from flask_session import Session
app = Flask(__name__)

import re
import requests
app.secret_key = 'dljsaklkszhfjhFSDHFuiewh4i325hjnflFNj'
app.jinja_env.filters['zip'] = zip

 

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/get_names' , methods = ["GET" , "POST"])
def get_names():
    data = request.get_json()
    session["name_list"] = data['all_names']
    # print(session["name_list"])
    return "got value"

@app.route('/get_graph_values' , methods = ["GET" , "POST"])
def get_graph_values():

    data_graph = request.form.to_dict(flat=False)

    # print((data_graph))
    gave_list = [ ]
    took_list = [ ]
    amount_list = [ ]
    
    for key in data_graph:
 
        if(re.search("gave", key) ):
            gave_list.append(str(data_graph[key][0]).strip())
        if(re.search("took", key) ):
            took_list.append(str(data_graph[key][0]).strip())
        if(re.search("amount", key) ):
            amount_list.append(str(data_graph[key][0]).strip())

    # print(gave_list , took_list , amount_list)

    names_list = [str(num) for num in session['name_list']]

    # print(names_list)

    return render_template("springify.html" , name_list = names_list , gave_list = gave_list , took_list = took_list , amount_list = amount_list)



    



if __name__ == "__main__":
    app.run(debug = True )
