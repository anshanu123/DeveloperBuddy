"""
Web Server code
"""
from flask import Flask, request, redirect

@app.route('/add_to_database', methods=['POST'])
def add_to_database():
    """adds a Developer Buddy custom plugin to the backend store
    Needs many parameters including: intent_schema, function, sample_utterances, params, etc."""
    function_code = request.form['function']
    params = request.form['params']

    # add more params here... 
    # process
    # submit to database
    # send response of successful or failure of addition

    """if not list_name or list_name is None or list_name is "":
        list_name = tag_name
    message_body = request.form['message_body']

    resp = process(tag_name, list_name, message_body)"""
    return str("done")



@app.route('/get_entry', methods=['GET'])
def get_entry():
    """gets a custom entry from the backend store based on the provided intent_name"""
    intent_name = request.args.get('intent_name')
    # get from data with intent_name as key
    # return

    return str(intent_name)



@app.route('/process_intent', methods=['GET'])
def process_intent():
    """processes intent from lambda functions and sends formatted request with function and params to sublime plugin"""
    intent_name = request.args.get('intent_name')
    # get params
    #send details through rest to the sublime plugin
    #get and process response from sublime plugin for alexa (returned)

    return str(intent_name)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8080)