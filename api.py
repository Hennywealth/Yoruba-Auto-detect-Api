from flask import Flask, render_template, request, redirect,abort,flash, make_response
import os
from flask.json import jsonify
import Spell_Detector
from AutoCorrect import SpellChecker

app = Flask(__name__)


@app.route("/api/search", methods=["GET", "POST"])
def show():
    parser = SpellChecker("dictionary.txt")

    if request.method == "POST":
        request_data = request.get_json(force=True)
        print("FORM DATA RECEIVED", request_data)
        Json_to_Dict_Data = request_data['search_word']
        result_dict = parser.check(Json_to_Dict_Data)
        return make_response(jsonify(result_dict), 200)
        
    return None

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

 

if __name__ == '__main__':
    app.run(debug=True)


