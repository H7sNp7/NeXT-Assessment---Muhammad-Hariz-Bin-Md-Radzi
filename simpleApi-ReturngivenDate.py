from flask import *
import json, time

app= Flask(__name__)

@app.route('/', methods=['GET'])

def home_page():

    data_set = {'Owner': 'MUHAMMAD HARIZ BIN MD RADZI' , "ISS Trivia" : "Malaysia have sent 1 Astronaut to the ISS","timestamp":time.time()}
    
    json_dump=json.dumps(data_set)

    return json_dump



@app.route('/tarikh/', methods=['GET'])

def req_page():

    tarikh=str(request.args.get('tarikh')) # /date/?date=#####

    data_set = {'Owner': 'MUHAMMAD HARIZ BIN MD RADZI' ,'Date Received :': f"Date received from the user UwU = {tarikh}"}
    
    json_dump=json.dumps(data_set)

    return json_dump


if __name__=='__main__':
    app.debug = True
    app.run(port=7777)