
from flask import Flask, request, render_template


country_capital_table = {}


try:
    with open('caps.txt') as f:
        while True:
            line = f.readline()

            if len(line)>2:
                splitted_line = line.split(",")
                splitted_line[0] = splitted_line[0].lower()
                splitted_line[1] = splitted_line[1].lower()

                if splitted_line[0] not in country_capital_table.keys():
                    country_capital_table[splitted_line[0]] = splitted_line[1][:-1]

                else:
                    pass

            else:
                break
except IOError:
    print('Could not find the file.')



app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error = e)

@app.route('/')
def my_form():
    try:
        return render_template('index.html')
    except Exception as e:
        return render_template('error.html', error = e)


@app.route('/', methods=['POST'])
def my_form_post():
    country = request.form['text']

    if country.isalpha():
        country = country.lower()

        if country in country_capital_table.keys():
            return country_capital_table[country].upper()

        else:
            return 'Seems this country does not exist.\nPlease enter the correct country name.'

    else:
        return 'Please enter the name in English!'