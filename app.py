from flask import Flask, request, render_template

table = {}
with open('caps.txt') as f:
    while True:
        line = f.readline()

        if len(line)>2:
            temp = line.split(",")
            temp[0] = temp[0].lower()
            temp[1] = temp[1].lower()
            if temp[0] not in table.keys():
                table[temp[0]] = temp[1][:-1]

        else:
            break

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    country = request.form['text']

    if country.isalpha():
        country = country.lower()
        if country in table.keys():
            return table[country].upper()

        else:
            return 'Seems this country does not exist.\nPlease enter the correct country'
    else:
        return 'Please the name in English!'