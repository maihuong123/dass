from flask import Flask, render_template
import mongoengine
from mongoengine import Document, StringField

host = "ds011893.mlab.com"
port = 11893
db_name = "c4e_rss"
user_name = "c4e"
password = "codethechange"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

class Project(Document):
    title = StringField()
    img = StringField()
    description = StringField()

m = Project(
    title = " DAS Diet",
    img = "http://dasdiet.vn/images/Gallery/13112011225962logomedium.jpg",
    description = "Weight loss by low car - high fat method"
)

m.save()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("das.html", das_list = Project.objects)


if __name__ == '__main__':
    app.run()

