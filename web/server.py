"""
Web Server code
"""
from flask import Flask, request, redirect

@app.route('/add_to_database', methods=['POST'])
def add_to_database():
    """processing handle for alexa app"""
    function_code = request.form['function']
    params = request.form['params']
    # add more params here... 
    # submit to database


    """if not list_name or list_name is None or list_name is "":
        list_name = tag_name
    message_body = request.form['message_body']

    resp = process(tag_name, list_name, message_body)"""
    return str("done")



@app.route('/get_entry', methods=['GET'])
def get_entry():
    """processing handling for alexa AllListsFromTagIntent intent"""
    intent_name = request.args.get('intent_name')

    return str(intent_name)



@app.route('/process_intent', methods=['GET'])
def process_intent():
    """processing handling for alexa AllListsFromTagIntent intent"""
    intent_name = request.args.get('intent_name')

    return str(intent_name)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8080)