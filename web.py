from flask import make_response, request
import flask
import json
import time
import subprocess
from trigger import trigg

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def web():
    code = '<script>function openform(){ document.getElementById("lform").style.display = "block"; document.getElementById("butt").style.display = "none"; }</script>'
    code += '<center style="font-family: Arial, Helvetica, sans-serif;"><h4>Check_this_out: <a href="https://epicgamesfree4all.herokuapp.com/" target="new" style="text-decoration: none;">Link</a></h4>'
    code += '<h2>Purchased_list</h2>'
    code += '<div id="lform" style="display: none;"><form method="POST" action="/send_data" target="_parent"><input type="text" name="username" placeholder="Username" required /><br /><input type="password" name="password" placeholder="Password" required /><br /><input type="submit" style="background: blue; color: white; padding: 8px; font-size: large;" /></form></div><input type="button" value="Run_now" onclick="openform()" id="butt" style="overflow: hidden;display: block;background: blue;color: white; padding: 8px; font-size: large; opacity: 0.4;"/>'
    code += '<table border="0" style="border-collapse: collapse; width: 80%; margin: 1.5em; font-size: 1em;">'
    for i in open('src/data.txt', 'r').readlines():
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

@app.route('/send_data', methods=['POST'])
def trig():                                             # To run it manually.
    username = request.form['username']
    password = request.form['password']
    code = "<center>"
    if username == 'admin' and password == '123':       # change it if you want to.
        trigg()
        code += '<p style="text-align: justify;">'
        with open('src/bot.log', 'r') as b:
            for l in b.readlines():
                code += l
                code += '<br />'
        code += '</p>'
    else:
        code += '<h1>Kinda_sus... Code: 666</h1>'

        code += '</center>'
    return make_response(code, 200)

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
