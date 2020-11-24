from flask import make_response
import flask
import json

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def web():
    code = '<center style="font-family: Arial, Helvetica, sans-serif;"><h4>Check_this_out: <a href="https://epicgamesfree4all.herokuapp.com/" target="new" style="text-decoration: none;">Link</a></h4>'
    code += '<h2>Purchased_list</h2>'
    code += '<table border="0" style="border-collapse: collapse; width: 80%; margin: 1.5em; font-size: 1em;">'
    for i in open('data.txt', 'r').readlines():
        if i != '\n':
            dta = json.loads(i)
            code += '''<tr style="border-bottom: 2px solid black; background: lightgray;">
                            <td>
                                <img src="{0}" style="height: 25%; width: auto;"/>
                            </td>
                            <td align="center" style="font-weight: bolder;font-size: larger;">
                                {1}
                            </td>
            </tr>'''.format(dta['thumbnail'], dta['title'])

    code += '</table></center>'
    
    return make_response(code, 200)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
