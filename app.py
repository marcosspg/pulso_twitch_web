from webbrowser import get
from flask import Flask, render_template, request
import csv


iduserdata = 0;
app = Flask(__name__);

temporalFolder = "o&w2e47R$!ad"
temporalFile = "pwlahsydi"

currentPath = __file__.replace("\\", "/").replace("app.py", "");

try:
    with open(currentPath+"results.txt") as inp:
        lines = inp.readlines()
        iduserdata = int(lines[lines.__len__()-1].split(";")[0])+1;
        inp.close();
except Exception as e:
    iduserdata = 0;




@app.route("/")
def index():
    return render_template("index.html");

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html");

@app.route("/svdt", methods = ['POST', 'GET'])
def svdt():
    global iduserdata;
    try:
        u = request.form.get("u").replace(";", "");
        pts = request.form.get("pts")
        string = str(iduserdata)+";"+u+";"+pts+";"+datetime.now().strftime('%d/%m/%Y')+"\n";
        with open(currentPath+"results.txt", "a") as out:
            out.write(string);
            
            iduserdata+=1;
    except Exception as e:
        print(e);
        None
    return "";

from datetime import datetime




@app.route("/getresults")
def getResults():
    try:
        u = request.form.get("us")
        p = request.form.get("pw")
        if u == temporalFile and p == temporalFolder:
            return readResults();
    except Exception as e:
        None
    return "";


def readResults():
    toReturn = "";
    
    with open(currentPath+"results.txt", encoding="utf-8") as inp:
        toReturn = inp.read();
        inp.close();
    return toReturn;

if __name__ == "__main__":
    #app.run(host="192.168.1.94");
    app.run(debug=True);