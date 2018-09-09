from flask import Flask, request, url_for, redirect
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():

    if request.method == 'POST':
        result = request.args.get('options')
        if result == 'index':

            return url_for('result', options=result)

        elif result == 'type':

            return url_for('result', options=result)

        else:
            return 'Invalid Options : Please select another options ["index", "type"]'

        return result

    else:
        return 'Invalid Reqeusts'

    return '404'


@app.route('/result/<options>', methods=['GET'])
def result(options=None):

    if request.method == 'GET':
        if options == 'index':
            return '1'
        elif options == 'type':
            return '2'
        else:
            return 'Invalid Search options'


        return options

    else:
        return 'Invalid Reqeusts'

    return '404'




if __name__ == '__main__':
    app.run(debug=True)