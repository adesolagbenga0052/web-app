from flask import Blueprint, render_template
from app import dataBank

link = Blueprint('link',__name__)

@link.get('/')
def index():
    return render_template('index.html')

@link.get('/test')
def test():
    group = [
        ]
    no = {"name":"no",'points':[]}
    nox = {"name":"nox",'points':[]}
    for data in dataBank:
        if data["SiteID"] == "500":
            date = data['Date Time'].split(":")[0].split("T")[0].replace("-","/")
            no["points"].append([date,float(data["NO"])]) if data["NO"] != "" else ""
            nox["points"].append([date,(data["NOx"])]) if data["NOx"] != "" else ""
    group.append(no)
    group.append(nox)
    return render_template('location.html',data={"graph1":group})
        

  