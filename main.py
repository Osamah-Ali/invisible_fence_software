import sys
from flask import Flask, jsonify, request, render_template
import time
from flask_socketio import SocketIO, emit
import sqlite3
from classes.pole_list import pole_list
from classes.pole import pole


poles= pole_list()
poles.add_to_head(pole(battary=55, temperature= 36, ip_addr= '192.168.100.2'))
poles.add_to_head(pole(battary=35, temperature= 20, ip_addr= '192.168.100.3'))
poles.add_to_head(pole(battary=7, temperature= 30, ip_addr= '192.168.100.4'))

app= Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/', methods= ['GET'])
def index():
    h= poles.tail
    items= []
    while (h != None):
        items.append([h.battary, h.temperature, h.ip_addr])
        h= h.behind_pole

    return render_template('index.html', items= items) 

@app.route('/pole_summary', methods= ['GET'])
def pole_summary():
    h= poles.tail
    items= []
    while (h != None):
        items.append([h.battary, h.temperature, h.ip_addr])
        h= h.behind_pole

    
    return render_template('pole_summary.html', items= items)

@app.route('/logs', methods= ['GET'])
def logs():
    conn= sqlite3.connect('logs.db')
    cur= conn.cursor()
    query= 'select * from logs'
    cur.execute(query)
    data= cur.fetchall()
    conn.close()
    return render_template('logs.html', items= data)



@app.route('/alarm', methods= ['POST'])
@socketio.on('message')
def alarm():
    data= request.form.get('data')
    print(f"data received {data}")
    socketio.emit('notification', {'data':data})
    return 'message received'

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    time.sleep(5)
    return jsonify({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))