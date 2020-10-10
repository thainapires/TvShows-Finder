from flask import Flask, render_template, request, url_for
import random, requests
import json

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html', randn = str(random.randint(4001,5000)))

@app.route('/requ')
def requ():
    response = requests.get("http://api.tvmaze.com/search/shows?q={}".format("House"))
    #jprint(response.json()[1])
    response = response.json()
    tvshow =[]
    for i in range(4):
        img = response[i]["show"]["image"]["original"]
        name = response[i]['show']['name']
        year = response[i]['show']['premiered']
        if(year == None):
            year = '-'
        else:
            year = year[0:4]
        time = response[i]['show']['schedule']['time'][0:2]
        genres = response[i]['show']['genres']
        summary = response[i]['show']['summary']
        if(summary == None):
            summary = '-'
        else:
            summary = summary.replace('<p>', '').replace('</p>', '')
        website = response[i]['show']['officialSite']
        rating = response[i]['show']['rating']['average']
        tvshow.append([
            img, name, year, time, genres, summary, website, rating
        ]
        )
    return render_template('movies.html', randn = str(random.randint(101,4000)), tvshows = tvshow)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

if __name__ == "__main__":
    app.run(debug=True)