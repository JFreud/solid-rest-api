from flask import Flask, render_template
import urllib2, json

api_app = Flask (__name__)

u = urllib2.urlopen("http://api.nasa.gov/planetary/apod?api_key=S93VcKmv5nCKEmbxi3459T5wo5UkuOrwDdT3vghB")
not_dict = u.read()
real_dict = json.loads(not_dict)

#getting error urllib2.URLError: <urlopen error EOF occurred in violation of protocol (_ssl.c:590)>

# r = requests.get("https://api.nasa.gov/planetary/apod?api_key=S93VcKmv5nCKEmbxi3459T5wo5UkuOrwDdT3vghB")
# real_dict = json.loads(r.json())

@api_app.route("/")
def root():

    return render_template("root.html", url = real_dict["hdurl"], text = real_dict["explanation"])


if __name__ == "__main__":
    api_app.run(debug=True)
