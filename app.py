from flask import Flask, render_template, request, redirect,abort,flash, make_response
import os
from flask.json import jsonify
from AutoCorrect import SpellChecker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api", methods=["GET", "POST"])
def show():
    parser = SpellChecker("dictionary.txt")

    if request.method == "POST":
        request_data = request.get_json(force=True)
        print("FORM DATA RECEIVED", request_data)
        json_to_dict_data = request_data['search_word']
        result_dict = parser.check(json_to_dict_data)
        return make_response(jsonify(result_dict), 200)
        
    
if __name__ == '__main__':
    app.run(debug=True)


