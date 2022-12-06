from flask import Flask,jsonify, request
import csv
all_movies = []
with open('movies.csv',encoding = 'utf8')as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

app = Flask(__name__)
@app.route('/get-movie')
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

app.run()