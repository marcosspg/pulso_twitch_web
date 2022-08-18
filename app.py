from flask import Flask, render_template

app = Flask(__name__);

@app.route("/")
def index():
    nombre = "paco";
    edad = 35;
    return render_template("index.html", nombre=nombre, edad=edad);



if __name__ == "__main__":
    app.run(debug=True);