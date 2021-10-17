from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first = ""
    return render_template('index.html', message = first)

@app.route('/alp')
def my_list():
    second = ["Alp", "Selman", "Samet"]
    return render_template('body.html', object = second)

      





if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)