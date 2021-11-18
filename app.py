from flask import Flask, redirect, url_for, render_template, request, flash, make_response
import psycopg2

conn = psycopg2.connect("host=10.101.51.62 dbname=npcapp user=pi password=qwe")
cursor = conn.cursor()
cursor.execute('SELECT * FROM npc')
dbReturn = cursor.fetchall()
cursor.close()
app= Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/searchnpc', methods=['POST', 'GET'])
def searchNpc():
    return render_template('searchnpc.html')
@app.route('/addnpc', methods=['POST', 'GET'])
def addNpc():
    npcName = request.args.get('name')
    npcCity = request.args.get('city')
    npcDescription = request.args.get('description')
    print(npcName)
    print(npcCity)
    print(npcDescription)

    return render_template('addNpc.html')

@app.route('/searchcity', methods=['POST', 'GET'])
def searchCity():
    return render_template('searchcity.html')
@app.route('/addcity', methods=['POST', 'GET'])
def addCity():
    return render_template('addcity.html')

@app.route('/browsecities', methods=['POST', 'GET'])
def browseCities():
    conn = psycopg2.connect("host=10.101.51.62 dbname=npcapp user=pi password=qwe")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM city')
    dbReturn = cursor.fetchall()
    cursor.close()
    return render_template('browsecities.html', cities=dbReturn)

@app.route('/browsenpcs', methods=['POST', 'GET'])
def browseNpcs():
    conn = psycopg2.connect("host=10.101.51.62 dbname=npcapp user=pi password=qwe")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM npc')
    dbReturn = cursor.fetchall()
    cursor.close()
    return render_template('browsenpcs.html', npcs=dbReturn)


@app.route('/offlinetest', methods=['GET', 'POST'])
def offlinetestIndex():
    return

if __name__ == "__main__":
  app.run(debug=True)