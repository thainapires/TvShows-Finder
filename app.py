from flask import Flask, render_template, request, url_for
import random, requests
import json

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html', randn = str(random.randint(4001,5000)))

@app.route('/about') 
def about():
    return render_template('about.html', randn = str(random.randint(4001,5000)))

@app.route('/search_tvshow', methods=['GET','POST'])
def search_tvshow():
    search_term = ''
    if request.method == 'POST':
        search_term = request.form['search_term']
        if(search_term == ''):
            return render_template('movies.html', randn = str(random.randint(101,4000)))
    response = requests.get("http://api.tvmaze.com/search/shows?q={}".format(search_term))
    #jprint(response.json()[1])
    response = response.json()
    #print(type(response))
    tvshow =[]
    if(not response):
        return render_template('movies.html', randn = str(random.randint(101,4000)))
    jprint(response)
    for i in range(len(response)-1):
        img = response[i]["show"]["image"]
        if(img == None):
            img = "../static/img_404.jpg"
        else:
            img = img["original"]
        name = response[i]['show']['name']
        if(name == None):
            name = 'not found'
        year = response[i]['show']['premiered']
        if(year == None):
            year = '-'
        else:
            year = year[0:4]
        time = response[i]['show']['schedule']['time'][0:2]
        if(time == None):
            time = '0'
        genres = response[i]['show']['genres']
        if(genres == None):
            genres = 'not found'
        summary = response[i]['show']['summary']
        if(summary == None):
            summary = '-'
        else:
            summary = summary[0:110]+'...'.replace('<p>', '').replace('</p>', '').replace('<b>', '').replace('</b>', '')
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