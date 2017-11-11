from flask import Flask, render_template, request
import urllib2, json


api_app = Flask (__name__)



#getting error urllib2.URLError: <urlopen error EOF occurred in violation of protocol (_ssl.c:590)>

# r = requests.get("https://api.nasa.gov/planetary/apod?api_key=S93VcKmv5nCKEmbxi3459T5wo5UkuOrwDdT3vghB")
# real_dict = json.loads(r.json())

@api_app.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=S93VcKmv5nCKEmbxi3459T5wo5UkuOrwDdT3vghB")
    not_dict = u.read()
    real_dict = json.loads(not_dict)

    
       
    return render_template("root.html", url = real_dict["hdurl"], text = real_dict["explanation"])


@api_app.route("/subs")
def do_tube():
    handle = request.args['handle']
    utube = urllib2.urlopen("https://www.googleapis.com/youtube/v3/channels?key=AIzaSyATP2BxeFJ1vx1o9k-48pLcBcAMopDf3PY&part=statistics&forUsername=%s" % handle).read()

    tube_dict = json.loads(utube)
    return tube_dict['items'][0]['statistics']['subscriberCount'] + " subscribers"
 

if __name__ == "__main__":
    api_app.run(debug=True)
