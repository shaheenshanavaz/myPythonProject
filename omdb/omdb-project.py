import requests
from flask import Flask,jsonify,request
import pprint as pp

# API_KEY = "b582cbe3"
# omdb_endpoint = f"http://www.omdbapi.com/?apikey={API_KEY}"
# param = {
#      "s" : "Fast & Furious",
# }
# response = requests.get(url=omdb_endpoint, params=param)
app = Flask(__name__)
result = ["Fast and Furious","kunfu panda"]
watchlist = []

@app.route("/movies",methods=['GET'])
def hello_world():
    return jsonify({'values':result})

# @app.route('/incomes', methods=['POST'])
# def add_income():
#   incomes.append(request.get_json())
#   return '', 204

@app.route("/favorites", methods=['POST'])
def watchlist():
    data = result.append(request.get_json())
    movievalues = data['values']
    watchlist.append(movievalues)
    return jsonify({'mywatchlist':watchlist})

if __name__ == "__main__":
    app.run(debug=True)