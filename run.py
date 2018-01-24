from random import *
from flask_cors import CORS
from threading import Lock
import urllib.parse

import requests
from flask import Flask, render_template, session, request, Response, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
import json
import os
from contextlib import closing

from flask import g

async_mode = None


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(A',
        block_end_string='A)',
        variable_start_string='(B',
        variable_end_string='B)',
        comment_start_string='(C',
        comment_end_string='C)',
    ))


app = CustomFlask(__name__,
                  static_folder="./dist/static",
                  template_folder="./dist")
# app = CustomFlask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_STATIC_TXT = os.path.join(APP_ROOT, 'static/jsons')  # 设置一个专门的类似全局变量的东西

v2config = []
v2pageconfig = []
with open(os.path.join(APP_STATIC_TXT, 'v2click.json'), encoding='utf-8') as f:
    s = f.readlines()  # 读取前五个字节

    doc = json.loads(''.join(s))
    v2config = doc
    f.close()
with open(os.path.join(APP_STATIC_TXT, 'v2page.json'), encoding='utf-8') as f:
    s = f.readlines()  # 读取前五个字节

    doc = json.loads(''.join(s))
    v2pageconfig = doc
    f.close()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)

        count += 1



@app.route('/api/h5')
def h5md():
    return render_template("READMEH5.md")

@app.route('/toorv1')
def toorv1():
    return render_template("toolv1.html")


@app.route('/api/clickitems/v2')
def clickitems_v2():
    with open(os.path.join(APP_STATIC_TXT, 'v2clickitems.json'), encoding='utf-8') as f:
        s = f.readlines()

        doc = json.loads(''.join(s))
        f.close()
    return jsonify(doc)


@app.route('/api/click/v2')
def click_v2():
    with open(os.path.join(APP_STATIC_TXT, 'v2click.json'), encoding='utf-8') as f:
        s = f.readlines()
        doc = json.loads(''.join(s))
        # v2config = doc

        tse = {
            # 'URL': "init"
        }
        for i in range(len(doc)):
            # print(" v2config:", v2config[i], '-->File "app.py", line 169')
            key1 = v2config[i]['参数']
            # v2config[i][key1] = argu.get(key1, 'error')
            tse[key1] = key1

        f.close()
    return jsonify(tse)


@app.route('/api/page/v2')
def click_v2page():
    with open(os.path.join(APP_STATIC_TXT, 'v2page.json'), encoding='utf-8') as f:
        s = f.readlines()

        doc = json.loads(''.join(s))
        v2pageconfig = doc

        tse = {
            # 'URL': "init"
        }
        for i in range(len(doc)):
            # print(" v2config:", v2config[i], '-->File "app.py", line 169')
            key1 = v2pageconfig[i]['参数']
            # v2config[i][key1] = argu.get(key1, 'error')
            tse[key1] = key1

        f.close()
    return jsonify(tse)


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@socketio.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'URL': message['data'], 'ID': session['receive_count']})


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    # emit('my_response',
    #      {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


@socketio.on('connect', namespace='/test')
def test_connect():
    g.con = 0
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


    emit('init')


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)
    emit('disconnect')


@app.route('/', defaults={'url': ''})
@app.route('/<path:url>', methods=['GET', 'POST'])
def home(url):
    # print(" request.url):", request.url, '-->File "run.py", line 211')

    isaudio = ("t2" in request.url)
    isv2page = ("p1=" in request.url)

    isv1 = ("session" in request.url)
    # return render_template("index.html")

    isvue = ("9527" in request.url)
    print(" isvue:", isvue, '-->File "run.py", line 189')
    print(" isvue:", isvue, '-->File "run.py", line 189')
    print(" isvue:", isvue, '-->File "run.py", line 189')
    print(" isvue:", isvue, '-->File "run.py", line 189')
    print(" isvue:", isvue, '-->File "run.py", line 189')
    print(" isvue:", isvue, '-->File "run.py", line 189')

    print(" app.debug:", app.debug, '-->File "run.py", line 189')
    print(" app.debug:", app.debug, '-->File "run.py", line 189')
    print(" app.debug:", app.debug, '-->File "run.py", line 189')
    print(" app.debug:", app.debug, '-->File "run.py", line 189')
    print(" app.debug:", app.debug, '-->File "run.py", line 189')
    print(" app.debug:", app.debug, '-->File "run.py", line 189')
    print(" app.debug:", app.debug, '-->File "run.py", line 189')

    if isvue:
        if app.debug:
          return requests.get('http://localhost:8080/{}'.format(url)).text
        else:
          return render_template("index.html")

    # if app.debug:
    #     return requests.get('http://localhost:8080/{}'.format(url)).text
    # else:
    #     return render_template("index.html")



    ish5 = ("stat.ajmide.com/m.gif" in request.url)
    isstatic = ("stat.ajmide.com" in request.url)

    if ish5:

        if True:
            argu = request.args

            tse = {
                'ID': -1,
                'URL': request.url,
                'body': urllib.parse.unquote(str(request.get_data()))
            }
            values = argu.get('ajmd', 'error')
            data = json.loads(values)


            for i in range(len(v2config)):
                key1 = v2config[i]['参数']

                # v2config[i][key1] = data.get(key1, 'error')
                tse[key1] = data.get(key1, 'error')


            socketio.emit('my_response',
                          tse,
                          namespace='/h5click')

    elif isstatic:

        if isv2page:

            argu = request.args

            tse = {
                'ID': -1,
                'URL': request.url,
                'body': urllib.parse.unquote(str(request.get_data()))
            }
            for i in range(len(v2pageconfig)):
                key1 = v2pageconfig[i]['参数']
                v2pageconfig[i][key1] = argu.get(key1, 'error')
                tse[key1] = argu.get(key1, 'error')

            socketio.emit('my_response',
                          tse,
                          namespace='/page')

        elif isv1:

            return ""

        elif isaudio:

            return ""

        elif (request.method == 'GET'):
            argu = request.args

            tse = {
                'ID': -1,
                'URL': request.url,
                'body': urllib.parse.unquote(str(request.get_data()))
            }
            for i in range(len(v2config)):
                # print(" v2config:", v2config[i], '-->File "app.py", line 169')
                key1 = v2config[i]['参数']
                v2config[i][key1] = argu.get(key1, 'error')
                tse[key1] = argu.get(key1, 'error')
                # print(" v2config:", v2config[i], '-->File "app.py", line 169')
            # print(" v2config:", v2config, '-->File "app.py", line 173')


            socketio.emit('my_response',
                          tse,
                          namespace='/test')

        elif (request.method == 'POST'):
            return ""

    with closing(

            requests.request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False)
    ) as resp:
        resp_headers = []
        for name, value in resp.headers.items():

            if name.lower() == 'connection':
                resp_headers.append((name, 'close'))

            if name.lower() in ('content-length', 'connection', 'content-encoding', 'transfer-encoding'):
                continue
            resp_headers.append((name, value))

        response = Response(resp.content, resp.status_code, resp_headers)

        return response


if __name__ == '__main__':
    # socketio.run(app, debug=True, port=5001)
    # socketio.run(app, debug=True, host="0.0.0.0", port=9527)

    print(" port:")
    socketio.run(app, host="0.0.0.0", port=9527)

