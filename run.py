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

# print(" APP_STATIC_TXT:", APP_STATIC_TXT, '-->File "app.py", line 40')
# print(" APP_STATIC_TXT:", APP_STATIC_TXT, '-->File "app.py", line 40')
# print(" APP_STATIC_TXT:", APP_STATIC_TXT, '-->File "app.py", line 40')

v2config = []
with open(os.path.join(APP_STATIC_TXT, 'v2click.json'), encoding='utf-8') as f:
    s = f.readlines()  # 读取前五个字节

    doc = json.loads(''.join(s))
    v2config = doc
    f.close()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)

        count += 1


# @app.route('/', defaults={'path': ''})
# def catch_all(path):
#     print(" path:", path, '-->File "run.py", line 72')
#     print(" path:", path, '-->File "run.py", line 72')
#     print(" path:", path, '-->File "run.py", line 72')
#     print(" path:", path, '-->File "run.py", line 72')
#
#     if app.debug:
#         return requests.get('http://localhost:8080/{}'.format(path)).text
#     return render_template("index.html")


@app.route('/api/toorv1')
def toorv1():
    return render_template("toolv1.html")


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
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('close_room', namespace='/test')
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])


@socketio.on('my_room_event', namespace='/test')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
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

    tse = {
    }
    for i in range(len(v2config)):
        # print(" v2config:", v2config[i], '-->File "app.py", line 169')
        key1 = v2config[i]['参数']
        # v2config[i][key1] = argu.get(key1, 'error')
        tse[key1] = key1

    emit('my_response', tse)
    emit('init', tse)


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


# @app.route('/', defaults={'path': ''})
# def catch_all(path):
#     print(" path:", path, '-->File "run.py", line 72')
#     print(" path:", path, '-->File "run.py", line 72')
#     print(" path:", path, '-->File "run.py", line 72')
#     print(" path:", path, '-->File "run.py", line 72')
#
#     if app.debug:
#         return requests.get('http://localhost:8080/{}'.format(path)).text
#     return render_template("index.html")
@app.route('/', defaults={'url': ''})
@app.route('/<path:url>', methods=['GET', 'POST'])
def home(url):
    # print("  v2config:", v2config, '-->File "app.py", line 153')


    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" url:", url, '-->File "run.py", line 184')
    print(" request.url):", request.url, '-->File "run.py", line 211')
    print(" request.url):", request.url, '-->File "run.py", line 211')
    print(" request.url):", request.url, '-->File "run.py", line 211')
    print(" request.url):", request.url, '-->File "run.py", line 211')

    isvue = ("5001" in request.url)
    print(" isvue:", isvue, '-->File "run.py", line 217')
    print(" isvue:", isvue, '-->File "run.py", line 217')
    print(" isvue:", isvue, '-->File "run.py", line 217')
    print(" isvue:", isvue, '-->File "run.py", line 217')

    if isvue:
        return requests.get('http://localhost:8080/{}'.format(url)).text
    # return render_template("index.html")

    isstatic = ("stat.ajmide.com" in request.url)

    if (isstatic):
        if (request.method == 'GET'):
            argu = request.args

            tse = {
                'data': request.url,
                'count': 0,
                'body': urllib.parse.unquote(str(request.get_data()))
            }
            for i in range(len(v2config)):
                # print(" v2config:", v2config[i], '-->File "app.py", line 169')
                key1 = v2config[i]['参数']
                v2config[i][key1] = argu.get(key1, 'error')
                tse[key1] = argu.get(key1, 'error')
                # print(" v2config:", v2config[i], '-->File "app.py", line 169')
            # print(" v2config:", v2config, '-->File "app.py", line 173')

            print(" tse:", tse, '-->File "app.py", line 182')

            socketio.emit('my_response',
                          tse,
                          namespace='/test')

        if (request.method == 'POST'):
            print(" request.url:", request.args, '-->File "runProxy.py", line 12')
            # print(" request.method:", request.method, '-->File "app.py", line 127')

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

        # excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        # headers = [(name, value) for (name, value) in resp.raw.headers.items()
        #            if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, resp_headers)

        return response


if __name__ == '__main__':
    # socketio.run(app, debug=True, port=5001)
    socketio.run(app, debug=True, host="0.0.0.0", port=5001)
