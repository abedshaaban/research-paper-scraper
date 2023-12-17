from flask import Blueprint, render_template, request, jsonify
from func import get_google_data

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/get_q_results", methods=['POST'])
def get_q_results():
    q = request.get_json()

    result = get_google_data(q)

    return jsonify(result)
