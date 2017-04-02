#!flask/bin/python
from flask import Flask, jsonify, abort, make_response 

app = Flask(__name__)
#Retrieve real forecasts
forecasts = [
    {
        'id': 1,
        'title': u'ASAP Forecasts',
        'description': u'Forecasts flares in the next 24 hours', 
        'Flare': False
    },
    {
        'id': 2,
        'title': u'FORSPEF Forecasts',
        'description': u'Forecasts SEP/CME events', 
        'Flare': False
    }
]

@app.route('/ims/api/v1.0/forecasts', methods=['GET'])
def get_forecasts():
	return jsonify({'forecasts': forecasts})

@app.route('/todo/api/v1.0/forecasts/<int:forecast_id>', methods=['GET'])
def get_task(forecast_id):
    forecast = [forecast for forecast in forecasts if forecast['id'] == forecast_id]
    if len(forecast) == 0:
        abort(404)
    return jsonify({'forecast': forecast[0]})	

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
if __name__ == '__main__':
	app.run(debug = True)
