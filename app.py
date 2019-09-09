# import important libraries
from flask import Flask, request, render_template


country_capital_table = {}
# table to store the record of country and its capital

try:
    # opening file
    with open('caps.txt') as f:
        while True:
            line = f.readline()
            # reading one line of file at one time.

            if len(line)>2:
                # if any null string comes in then it will be avoided

                splitted_line = line.split(",")
                splitted_line[0] = splitted_line[0].lower()
                splitted_line[1] = splitted_line[1].lower()
                # changing everything to lower case, to make it simple to handle.

                if splitted_line[0] not in country_capital_table.keys():
                    country_capital_table[splitted_line[0]] = splitted_line[1][:-1]
                    # every line has one /n in last, [:-1] will exclude that last character.

                else:
                    pass

            else:
                break
except IOError:
    # IO error, if file does not find.
    print('Could not find the file.')



app = Flask(__name__)
# initialising the FlaskApp

@app.errorhandler(404)
def page_not_found(e):
    # default error handle, will take care of 404 error.
    return render_template('error.html', error = e)

@app.route('/')
def my_form():
    # home page of the app.
    try:
        return render_template('index.html')
    except Exception as e:
        return render_template('error.html', error = e)


@app.route('/', methods=['POST'])
def my_form_post():
    # function to receive data from the user and process further.

    country = request.form['text']
    # this data is coming from the html page.

    if country.isalpha():
        # check for input type. Is should be a string of characters only.
        country = country.lower()

        if country in country_capital_table.keys():
            return country_capital_table[country].upper()

        else:
            return 'Sorry! Invalid country name'

    else:
        return 'Please enter the name in English!'