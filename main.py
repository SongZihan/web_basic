from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello_world():
    return render_template('Frontend_basic.html')

@app.route('/another_page',methods=["GET"])
def another():
    return render_template('another_page.html')


if __name__ == "__main__":
    app.run(host="localhost")
