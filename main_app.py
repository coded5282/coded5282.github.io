from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index.html")
def indexa():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/publications.html")
def publications():
    return render_template('publications.html')

if __name__ == '__main__':
    app.run(debug=True)
