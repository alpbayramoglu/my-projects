from flask import Flask, render_template, request
from werkzeug.exceptions import MethodNotAllowed

app = Flask(__name__)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html", methods = ["GET"])

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

@app.route("/", methods = ["GET", "POST"])
def roman():
    if request.method == "POST":
        mynumber = request.form.get("number")

        if mynumber.isnumeric() and int(mynumber) > 1 and int(mynumber) < 4000:
            return render_template("result.html",\
            number_decimal=mynumber, number_roman=convert(int(mynumber)), developer_name="Alp")             
    
        else:
           return render_template("index.html", not_valid=True) 


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)