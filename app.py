from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    subjects = ["Alex", "Bacho", "Gio",'Gela']
    return render_template('index.html', subjects=subjects, list=list)

@app.route("/<name>/<int:age>")
def user(name,age):
    return render_template('user.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
